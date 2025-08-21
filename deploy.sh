#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
# Get the Google Cloud project ID from your gcloud configuration.
export PROJECT_ID=$(gcloud config get-value project)

# Set the region where your resources will be created.
export REGION="us-central1"

# Set the name for your Artifact Registry repository.
export REPO_NAME="pageant-vision-repo"

# Set the name for your container image and Cloud Run service.
export IMAGE_NAME="pageant-vision-api"

# --- Main script ---

echo "--- Enabling required Google Cloud services... ---"
gcloud services enable run.googleapis.com \
    artifactregistry.googleapis.com \
    cloudbuild.googleapis.com

echo "--- Creating Artifact Registry repository (if it doesn't exist)... ---"
# The command will fail if the repository already exists, but 'set -e' is off for this command.
gcloud artifacts repositories create "$REPO_NAME" \
    --repository-format=docker \
    --location="$REGION" \
    --description="Repository for Pageant Vision API images" || echo "Repository '$REPO_NAME' already exists."

echo "--- Building and pushing the Docker image to Artifact Registry... ---"
gcloud builds submit --tag "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest"

echo "--- Deploying the image to Cloud Run... ---"
# This is a minimal deployment. It does not set any secrets or environment variables.
# The service will start, but API calls will likely fail until secrets are configured.
gcloud run deploy "$IMAGE_NAME" \
  --image "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest" \
  --platform managed \
  --region "$REGION" \
  --allow-unauthenticated

echo "--- Deployment complete! ---"
SERVICE_URL=$(gcloud run services describe "$IMAGE_NAME" --platform managed --region "$REGION" --format 'value(status.url)')
echo "Service URL: $SERVICE_URL"