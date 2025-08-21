# Mobile App Integration Guide

To communicate with the secured backend API, your mobile application must include the API key in every request.

## 1. Adding the API Key to HTTP Requests

For every API call your mobile app makes to the backend, you need to add an HTTP header:

-   **Header Name:** `X-API-Key`
-   **Header Value:** Your secret API key.

Most HTTP client libraries allow you to set default headers for all subsequent requests, which is a convenient way to implement this.

### Example HTTP Request

Here is what a raw HTTP request should look like.

```http
GET /api/v1/some-endpoint HTTP/1.1
Host: your-api-domain.com
Accept: application/json
X-API-Key: YOUR_SECRET_API_KEY_HERE
```

### Pseudocode Example

Here is a pseudocode example of how you might configure your HTTP client in your mobile app's code.

```
// Get the API key from a secure location
const apiKey = getApiKeyFromSecureStorage();

// Configure your HTTP client
const apiClient = new HttpClient({
  baseUrl: "https://your-api-domain.com",
  headers: {
    "X-API-Key": apiKey,
    "Content-Type": "application/json"
  }
});

// Now you can make requests without setting the header each time
const data = await apiClient.get("/api/v1/some-endpoint");
```

## 2. Securely Storing the API Key

**Do not hardcode the API key in your source code.** This is insecure as it can be easily extracted from your app package.

Instead, use a method to inject the key at build time:

-   **For React Native/Flutter:** Use a `.env` file and a library like `react-native-dotenv` or `flutter_dotenv` to load the key into your app's environment.
-   **For native iOS/Android:** Use build configurations (Xcode's `.xcconfig` files or Android's `build.gradle` with `buildConfigField`) to expose the key as a variable.

These methods keep the key out of version control and allow you to use different keys for development and production builds.
