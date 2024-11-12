# Contact list django rest api

<h3>ROUTES TO IMPLEMENT (ACCOUNT)</h3>

| METHOD   |                        ROUTE | FUNCTIONALITY                    |ACCESS|
|----------|-----------------------------:|----------------------------------| ------------- |
| *POST*   |      ```/account/profile/``` | _Register new user_              | _All users_|
| *POST*   |        ```/account/login/``` | _Login user_                     |_All users_|
| *GET*    |      ```/account/profile/``` | _Search accounts_                |_All users_|
| *GET*    | ```/account/profile/{id}/``` | _Account profile read_           | _All users_|
| *PUT*    |            ```/account/profile/{id}/``` | _Account profile update_         |_All users_|
| *PATCH*  |                 ```/account/profile/{id}/``` | _Account profile partial update_ |_All users_|
| *DELETE* |          ```/account/profile/{id}/``` | _Account profile delete_         | _All users_|

<h3>ROUTES TO IMPLEMENT (CONTACT LIST)</h3>

| METHOD   |                      ROUTE | FUNCTIONALITY        |ACCESS|
|----------|---------------------------:|----------------------| ------------- |
| *GET*    |        ```/contact/api/``` | _contact list_       | _All users_|
| *POST*   |           ```/contact/api/``` | _contact api create_ |_All users_|
| *GET*    | ```/contact/api/{contact_id}/``` | _contact api read_   |_All users_|
| *PUT*    | ```/contact/api/{contact_id}/``` | _contact api update_ | _All users_|
| *DELETE* | ```/contact/api/{contact_id}/``` | _contact api delete_ | _All users_|
