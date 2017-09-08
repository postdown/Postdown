# Example-Collection

----------------

## An example collection for postdown.

*This example could show you what's the postdown could do.*

----------------

## An example API with GET

```
GET http://0.0.0.0:8000/get/example?example-key=example-value
```

### An example API.

You should write the detail about this API.

**It's markdown supported.**

----------------

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |-|-|-|
> |example-key|example-value|example-description|
> 
> **Header**
> 
> |Key|Value|Description|
> |-|-|-|
> |example-header|example-header-value|example-description|
> 

### Examples:

> 
> **Example: This's a right way to use.**
> 
> > 
> > **Request**
> > 
> > > 
> > > **Query**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|successful|example-description|
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-header|example-header-value|example-description|
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |-|-|
> > > |connection|keep-alive|
> > > |content-length|23|
> > > |content-type|application/json|
> > > |keep-alive|60|
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "result": "successful"
> > > }
> > > ```
> > > 
> > 
> 
> **Example: This's the worry way to use.**
> 
> > 
> > **Request**
> > 
> > > 
> > > **Query**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|unsuccessful|example-description|
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-header|example-header-value|example-description|
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |-|-|
> > > |connection|keep-alive|
> > > |content-length|25|
> > > |content-type|application/json|
> > > |keep-alive|60|
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "result": "unsuccessful"
> > > }
> > > ```
> > > 
> > 
> 

----------------

## An example API with POST

```
POST http://0.0.0.0:8000/post/example?example-key=example-value
```

### An example API.

You should write the detail about this API.

**It's markdown supported.**

----------------

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |-|-|-|
> |example-key|example-value|example-description|
> 
> **Header**
> 
> |Key|Value|Description|
> |-|-|-|
> |example-header|example-header-value|example-description|
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |-|-|-|-|
> |example-key|example-value|text|example-description|
> 

### Examples:

> 
> **Example: Successful Request**
> 
> > 
> > **Request**
> > 
> > > 
> > > **Query**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|example-value|example-description|
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-header|example-header-value|example-description|
> > > 
> > > **Body**
> > > 
> > > |Key|Value|Type|Description|
> > > |-|-|-|-|
> > > |example-key|successful|text|example-description|
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |-|-|
> > > |connection|keep-alive|
> > > |content-length|25|
> > > |content-type|application/json|
> > > |keep-alive|60|
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "result": [
> > >     "successful"
> > >   ]
> > > }
> > > ```
> > > 
> > 
> 
> **Example: Unsuccessful Requests**
> 
> > 
> > **Request**
> > 
> > > 
> > > **Query**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|example-value|example-description|
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-header|example-header-value|example-description|
> > > 
> > > **Body**
> > > 
> > > |Key|Value|Type|Description|
> > > |-|-|-|-|
> > > |example-key|unsuccessful|text|example-description|
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |-|-|
> > > |connection|keep-alive|
> > > |content-length|27|
> > > |content-type|application/json|
> > > |keep-alive|60|
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "result": [
> > >     "unsuccessful"
> > >   ]
> > > }
> > > ```
> > > 
> > 
> 

----------------

## An example API with JSON

```
POST http://0.0.0.0:8000/json/example?example-key=example-value
```

### An example API.

You should write the detail about this API.

**It's markdown supported.**

----------------

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |-|-|-|
> |example-key|example-value|example-description|
> 
> **Header**
> 
> |Key|Value|Description|
> |-|-|-|
> |example-key|example-value|example-description|
> |Content-Type|application/json||
> 
> **Body**
> 
> ```
> {
> 	"example-key": "example-value"
> }
> ```
> 

### Examples:

> 
> **Example: Successful Request**
> 
> > 
> > **Request**
> > 
> > > 
> > > **Query**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|example-value|example-description|
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|example-value|example-description|
> > > |Content-Type|application/json||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > > 	"example-key": "successful"
> > > }
> > > ```
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |-|-|
> > > |connection|keep-alive|
> > > |content-length|23|
> > > |content-type|application/json|
> > > |keep-alive|60|
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "result": "successful"
> > > }
> > > ```
> > > 
> > 
> 
> **Example: Unsuccessful Request**
> 
> > 
> > **Request**
> > 
> > > 
> > > **Query**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|example-value|example-description|
> > > 
> > > **Header**
> > > 
> > > |Key|Value|Description|
> > > |-|-|-|
> > > |example-key|example-value|example-description|
> > > |Content-Type|application/json||
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > > 	"example-key": "unsuccessful"
> > > }
> > > ```
> > > 
> > 
> > **Response**
> > 
> > > 
> > > **Header**
> > > 
> > > |Key|Value|
> > > |-|-|
> > > |connection|keep-alive|
> > > |content-length|25|
> > > |content-type|application/json|
> > > |keep-alive|60|
> > > 
> > > **Body**
> > > 
> > > ```
> > > {
> > >   "result": "unsuccessful"
> > > }
> > > ```
> > > 
> > 
> 

----------------

----------------

Built with [Postdown][PyPI].

Author: [Titor](https://github.com/TitorX)

[PyPI]:    https://pypi.python.org/pypi/Postdown
