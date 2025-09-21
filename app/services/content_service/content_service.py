from app.services.database_service import DatabaseService
from app.models.hax_models.MediaOptionCard import MediaOptionCardFactory
from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper
from app.services.content_service import accesses_handler as accesses
from app.services.jwt_service import JWTService as jwt

class ContentService:
    @staticmethod
    def mux_thumbnail_url(mux_playback_id: str) -> str:
        # Stub: Replace with real JWT signing logic for Mux
        return f"https://image.mux.com/{mux_playback_id}/thumbnail.jpg?token=SIGNED_JWT"

    @staticmethod
    async def get_my_videos(user_id: int):

        #STEP 1 - Pull Data
        purchased_live_event_ids, purchased_category_ids = accesses.accesses_for(user_id)
        all_live_events = DatabaseService.get_future_videos()
        all_categories = DatabaseService.get_future_categories()
        #Filter categories to only those that have at least one video referencing them
        all_live_event_category_ids = set(str(event.category) for event in all_live_events if getattr(event, "category", None) is not None)
        all_categories = [cat for cat in all_categories if str(cat.id) in all_live_event_category_ids]
        
        #STEP 2 - Build Category Cards (& group into "Purchased" and "More Events")
        categories_purchased = [cat for cat in all_categories if str(cat.id) in purchased_category_ids]
        category_cards_purchased = [MediaOptionCardFactory.from_category(cat) for cat in categories_purchased]
        categories_more = [cat for cat in all_categories if str(cat.id) not in purchased_live_event_ids]
        category_cards_more = [MediaOptionCardFactory.from_category(cat) for cat in categories_more]
        all_category_cards = category_cards_purchased + category_cards_more

        #STEP 3 - Nest Events into Categories
        #loop through each live event in all_live_events. If the event has the category property and that property matches a category_card's id, then convert to MediaOptionCard and nest in the matching category_card's children property. If no match, then just convert to MediaOptionCard and add to top-level list.
        for next_live_event in all_live_events:
            category_id_reference = str(next_live_event.category)
            if category_id_reference is not None:
                found = False
                for cat_card in all_category_cards:
                    if not found and cat_card.id() == str(category_id_reference):
                        found = True
                        new_card = await MediaOptionCardFactory.from_live_event(next_live_event)
                        all_children = cat_card.data.children() or []
                        all_children.append(new_card.data)
                        cat_card.data.overwrite(incoming_children=all_children)
                        break
                if not found:
                    # No matching category found, add to top-level
                    new_card = MediaOptionCardFactory.from_live_event(next_live_event)
                    category_cards_more.append(new_card)
            else:
                # No matching category found, add to top-level
                new_card = MediaOptionCardFactory.from_live_event(next_live_event)
                category_cards_more.append(new_card)
        
        #update all_category_cards with potential new addtions we just added
        #all_category_cards = category_cards_purchased + category_cards_more
        purchased_list = MediaOptionCardFactory.embed_in_list(category_cards_purchased, "My Purchases")
        more_events_title = "More Events"
        if len(category_cards_purchased) == 0:
            more_events_title = "Upcoming Events"
        other_events_list = MediaOptionCardFactory.embed_in_list(category_cards_more, more_events_title)
        full_list = MediaOptionCardFactory.wrap_lists(list_of_card_lists=[purchased_list, other_events_list])

        #print("category card example")
        #print(all_category_cards[0].data.data)
        #return { "children" : [card.data.data for card in all_category_cards] }
        return full_list.data
    
    @staticmethod
    async def get_playback_token(mux_playback_id: str) -> str:
        return await jwt.create_mux_playback_token(playback_id=mux_playback_id)