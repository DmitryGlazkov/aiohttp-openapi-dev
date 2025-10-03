# users_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](DefaultApi.md#users_get) | **GET** /users | 
[**users_post**](DefaultApi.md#users_post) | **POST** /users | 
[**users_user_id_get**](DefaultApi.md#users_user_id_get) | **GET** /users/{user_id} | 


# **users_get**
> List[User] users_get()

Список пользователей

### Example


```python
import users_client
from users_client.models.user import User
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.DefaultApi(api_client)

    try:
        api_response = await api_instance.users_get()
        print("The response of DefaultApi->users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(user_create=user_create)

Создать пользователя

### Example


```python
import users_client
from users_client.models.user import User
from users_client.models.user_create import UserCreate
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.DefaultApi(api_client)
    user_create = users_client.UserCreate() # UserCreate |  (optional)

    try:
        api_response = await api_instance.users_post(user_create=user_create)
        print("The response of DefaultApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Получить пользователя

### Example


```python
import users_client
from users_client.models.user import User
from users_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = users_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with users_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_client.DefaultApi(api_client)
    user_id = 56 # int | 

    try:
        api_response = await api_instance.users_user_id_get(user_id)
        print("The response of DefaultApi->users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

