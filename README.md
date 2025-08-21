# Pageant Vision API

Backend service for Pageant Vision.

## Local Development

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    > **Note:** If you encounter a `ModuleNotFoundError`, please ensure you have activated your virtual environment and have run this command to install all required packages.

3.  **Run the application:**
    ```bash
    APP_ENV=staging uvicorn main:app --reload
    ```
    
    The application will be available at `http://127.0.0.1:8000`.

## Docker

### Build the image
```bash
docker build -t pageant-vision-api .
```

### Run the container
```bash
docker run -p 8080:8080 -e "API_KEY=your_api_key" pageant-vision-api
```
The application will be available at `http://localhost:8080`.

## Deployment to Google Cloud Run

This assumes you have `gcloud` CLI installed and configured.

1.  **Enable services:**
    ```bash
    gcloud services enable run.googleapis.com
    gcloud services enable artifactregistry.googleapis.com
    ```

2.  **Build and push the image to Artifact Registry:**
    ```bash
    export PROJECT_ID=$(gcloud config get-value project)
    export REGION=us-central1 # Or your preferred region
    export REPO_NAME=pageant-vision-repo
    export IMAGE_NAME=pageant-vision-api

    # Create repository if it doesn't exist
    gcloud artifacts repositories create $REPO_NAME --repository-format=docker --location=$REGION

    # Build and push
    gcloud builds submit --tag $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest
    ```

3.  **Deploy to Cloud Run:**
    ```bash
    # Store your API key in Secret Manager
    echo "your_secret_api_key" | gcloud secrets create api-key --data-file=-
    gcloud secrets add-iam-policy-binding api-key \
        --member="serviceAccount:$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com" \
        --role="roles/secretmanager.secretAccessor"


    # Deploy the service
    gcloud run deploy $IMAGE_NAME \
      --image $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest \
      --platform managed \
      --region $REGION \
      --allow-unauthenticated \
      --set-secrets="API_KEY=api-key:latest"
    ```
