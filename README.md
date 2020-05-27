# Task-TFL

### Live link - https://frozen-plains-48104.herokuapp.com/api/

REST API end point to get activity of users

## REST API Endpoints

**Activity Period with User Inforation (all)**
----
  List all activities along with user info

* **URL**

  `api/act-user/`

* **Method:**

  `GET`
  
**Activity Period with User Information (individual)**
----
  List all activities of a particular user, along with user info. Requires user id

* **URL**

  `api/act-user/<int:pk>/`

* **Method:**

  `GET`
  
*  **URL Params**
   
   **Required:**
 
   `[integer]`   

**User List**
----
  List and create all users

* **URL**

  api/users/

* **Method:**

  `GET` | `POST`
  
**User Details**
----
  Retrieve, update or delete a user

* **URL**

  api/users/<int:pk>/

* **Method:**

  `GET` | `PATCH` | `DELETE`
  
*  **URL Params**
   
   **Required:**
 
   `[integer]`

**Activity List**
----
  List and create activites

* **URL**

  `api/acitivities/`

* **Method:**

  `GET` | `POST`
  
**User Details**
----
  Retrieve, update or delete an activity

* **URL**

  `api/activities/<int:pk>/`

* **Method:**

  `GET` | `PATCH` | `DELETE`
  
*  **URL Params**
   
   **Required:**
 
   `[integer]`
