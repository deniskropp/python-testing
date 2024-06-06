## ClassDef sample_property
Doc is waiting to be generated...
### FunctionDef __init__(self, method, name)
**__init__**: The function **__init__** initializes the sample_property object. 

**parameters**: The parameters required by this function are as follows:

- self: A standard first parameter in Python methods, representing the instance of the class.
- method: The parameter that provides the method or function that will be associated with the sample_property object. It is expected to be a callable object, such as a function or another callable instance.
- name: An optional string parameter that allows you to specify a custom name for the sample_property. If not provided, the name of the associated method will be used as the default value.

**Code Description**: This function initializes the sample_property object by setting the "method" attribute to the provided "method" parameter. It also sets the docstring of the sample_property object to the docstring of the provided method, using the "method_docs" attribute. This is useful for documentation purposes, as it ensures that the sample_property object has the same documentation as the underlying method. Additionally, the function sets the "name" attribute of the sample_property object, either from the provided "name" parameter or, if not provided, from the name of the method. This allows for a custom or default name for the sample_property. 

**Note**: The **__init__** function is a critical part of the sample_property class, as it sets the foundational attributes that define the behavior and identity of the object. It is important to provide a "method" parameter, as this is what the sample_property object will be associated with and used for. The "name" parameter is optional but can be useful for providing a more descriptive or meaningful name for the sample_property, especially if it differs from the name of the underlying method.
***
### FunctionDef __get__(self, inst, cls)
**__get__**: The function **__get__** is used to retrieve the value of a property and perform additional operations on the retrieved result. 

**parameters**:
- self: The instance of the property class.
- inst: The instance of the class owning the property.
- cls: The class of the instance, 'inst'.

**Code Description**: This function is called when accessing a property of a class. It first checks if the instance, 'inst', is None, and if so, it returns the property object itself. This allows accessing the property directly on the class, rather than on an instance. 

If 'inst' is not None, the function proceeds to call the 'method' attribute of the property, passing 'inst' as an argument. The result of this method call is then processed. If the result is a list or a tuple, the function adds all the items in the result to the 'db' attribute of 'inst' using the 'add_all' method. Otherwise, if the result is a single object, it is added to the 'db' using the 'add' method. 

The function then updates the 'used_properties' set of 'inst' by adding the name of the property. This is likely used to track which properties have been accessed or modified. Finally, the result is set as an attribute of 'inst' with the same name as the property, and the result is returned. 

**Note**: This function assumes that the 'inst' object has a 'db' attribute, which is used to store the results. The 'add_all' and 'add' methods are expected to be defined for the 'db' attribute. 

**Output Example**: Let's assume the 'method' attribute of the property returns a list of two objects when called with 'inst'. The 'db' attribute of 'inst' would then contain these two objects after the **__get__** function is called. The property value, which is the result, would also be accessible as an attribute of 'inst' with the same name as the property.
***
### FunctionDef __call__(self, obj)
**__call__**: The function **__call__** invokes an underlying method on an object.

**parameters**:
- self: The instance of the class.
- obj: The object on which the method will be invoked.

**Code Description**: The **__call__** function is a special method in Python that allows an instance of a class to be called as if it were a function. In this case, when an instance of the class is called with an object obj, it invokes the self.method function on that object. The underlying method, self.method, is not defined within this code snippet, and its implementation details are not provided.

**Note**: The purpose of this function is to provide a convenient way to invoke a method on an object by calling an instance of a class. However, it is important to note that the actual behavior and return value will depend on the implementation of the self.method function.

**Output Example**: Assuming self.method is implemented to return a processed version of the input object, an output example could be:

```python
result = __call__(obj)
# If self.method returns the length of the object
# result would be the length of obj
```
***
## ClassDef Sample
Doc is waiting to be generated...
### ClassDef __metaclass__
Doc is waiting to be generated...
#### FunctionDef __new__(cls, cls_name, bases, attributes)
Doc is waiting to be generated...
***
***
### FunctionDef __init__(self, db)
**__init__**: The function initializes a Sample object.

**parameters**:
- self: A standard Python parameter referring to the instance of the class.
- db: The database connection or a ScopedSession object.
- kwargs: A dictionary of keyword arguments that will be added to the instance's dictionary (self.__dict__).

**Code Description**: This function initializes the Sample object by setting the database connection and additional keyword arguments. If a ScopedSession object is provided as the db argument, it accesses the underlying registry using db.registry() to obtain the actual database connection. The db attribute is then set to this connection.

Additionally, it initializes an empty set called used_properties, which is likely used to track the properties that have been accessed or utilized. Finally, it updates the instance's dictionary (self.__dict__) with the provided keyword arguments, allowing dynamic attribute assignment during object creation.

**Note**: The __init__ function is a crucial part of any class, as it initializes the object's state. In this case, it sets up the database connection and provides a way to pass additional arguments during object creation, enhancing flexibility and customization.
***
### FunctionDef create_all(self)
**create_all**: The function **create_all** is used to facilitate the creation of various database entities, including users, categories, roles, and SMIs (Shared Memory Identifiers?). 

**parameters**: 
- self: The instance of the class, allowing access to the class attributes and methods. 

**Code Description**: 
The **create_all** function plays a pivotal role in the project's testing phase, specifically in the creation and validation of database entities. It is invoked within multiple test cases in the "tests.py" module, each with a distinct focus. 

In the "test_sample_creation" test, the function is used to create a "DataSample" instance, which in turn generates a user ("john"), categories ("cat1" and "cat2"), an SMI ("newspaper"), and a role ("newspaper_editor") linked to the user and SMI. The test then proceeds to verify that the created entities match the expected results using "self.assertEqual". 

A similar pattern is observed in "test_sample_creation_with_scoped_session", "test_sample_creation_with_autocommit", and "test_sample_creation_using_scopedsession_with_autocommit". These tests explore the creation process within the context of scoped sessions and autocommit functionality, ensuring that the created entities are as expected. 

The "test_sample_creation_with_mixins" test introduces the concept of class inheritance and mixins. Here, the "DataSample" class inherits from both "SampleCat" and "Mixin", demonstrating how the **create_all** function can accommodate more complex class structures while still ensuring the accurate creation of entities. 

Additionally, the "test_sample_method_overriding" and "test_sample_method_overriding_with_call_to_base" tests validate the function's behavior when method overriding occurs. They confirm that the **create_all** function respects the overridden methods and creates entities based on the overridden behavior. 

The remaining tests, "test_sample_attr_returns_list" and "test_sample_attr_returns_tuple", focus on the nature of the "categories" attribute. They verify that the function correctly handles attributes that return lists or tuples of categories, ensuring that the created categories match the expected set. 

**Note**: 
The **create_all** function is a pivotal testing utility, enabling the validation of entity creation within the database. Its usage across various test cases demonstrates its flexibility in handling different class structures, inheritance, method overriding, and attribute variations.
***
## ClassDef Restorable
Doc is waiting to be generated...
### FunctionDef __init__(self, db, watch)
**__init__**: The function initializes a Restorable object.

**parameters**:
- self - The instance of the Restorable class.
- db - The database connection or a ScopedSession object. If a ScopedSession is provided, it is converted to a registry using the .registry() method.
- watch - Optional. The database to watch for changes. If not provided, it defaults to the db parameter value.

**Code Description**: This function initializes the Restorable object by setting the db, watch, and history attributes. The db parameter is used to establish a connection to the database and is stored as an attribute. If the db parameter is an instance of ScopedSession, it is converted to a registry using the .registry() method, which allows the Restorable object to access the database session and its associated configuration.

The watch parameter specifies the database to monitor for changes. If it is not provided, the db parameter is used as the default value for watch. This allows the Restorable object to observe and track changes made to the specified database.

The history attribute is initialized as an empty dictionary {}. It will be used to store the change history or state of the Restorable object. This history can include information about the object's attributes, modifications, or any other relevant data that needs to be tracked over time.

**Note**: The Restorable class appears to be designed for managing and tracking changes in a database or a specific database session. The __init__ function sets up the necessary attributes and connections to enable this change tracking functionality.
***
### FunctionDef __enter__(self)
**__enter__**: The function **__enter__** sets up an event listener to trigger the 'after_flush' event.

**parameters**:
- self: The instance of the 'Restorable' class.

**Code Description**:
The '**__enter__**' function is a part of the context management protocol, which is typically used with the 'with' statement in Python. In this case, it is utilized within the 'Restorable' class to establish a context for managing database operations.

When **__enter__** is called, it sets up an event listener using 'event.listen'. The listener is attached to the 'self.watch' event and configured to trigger the 'after_flush' function ('self.after_flush') specifically after a database flush event ('after_flush').

The 'after_flush' function, as described in its documentation, plays a crucial role in tracking new instances added to the database during a flush operation. It ensures that the 'history' attribute is updated with the identities of these new instances, enabling subsequent actions or rollbacks.

By invoking **__enter__**, the 'after_flush' function will be automatically triggered in response to a database flush event. This allows the 'Restorable' class to capture and record the necessary information about new instances, providing context for potential future operations or undo functionality.

**Note**: The **__enter__** function is a critical step in setting up the event listener for 'after_flush'. It ensures that the necessary infrastructure is in place for tracking new database instances.
***
### FunctionDef __exit__(self, type, value, traceback)
**__exit__**: The function **__exit__** performs cleanup operations when exiting a context, including database rollback, expunging all data, and removing event listeners. 

**parameters**:
- self: The instance of the 'Restorable' class.
- type: The type of the exception that occurred, if any.
- value: The value of the exception that occurred, if any.
- traceback: The traceback object providing information about the exception's origin.

**Code Description**: 
The **__exit__** function is an essential part of the context management protocol, defined by the 'with' statement in Python. It is called when exiting the context managed by the 'Restorable' class, and its primary purpose is to ensure proper cleanup, especially in the presence of exceptions. 

Within the function:
- A database rollback is performed to undo any changes made in the context.
- The db.expunge_all() method is called to remove all expunged instances from the session, ensuring no references to these instances remain.
- The autoflush setting of the database is temporarily disabled to prevent any automatic flush operations during cleanup.
- If the database is in autocommit mode, a new transaction is started to ensure subsequent operations are properly managed.
- The function iterates over the 'history' attribute, which is a dictionary containing class-level information about instances to be deleted. For each class and identifier set, it retrieves the corresponding instance from the database and deletes it if it exists.
- After performing the necessary deletions, a commit is issued to persist the changes, and the database connection is closed.
- Finally, the autoflush setting is restored to its original value, and the event listener for the 'after_flush' function is removed, ensuring no further tracking of new instances. 

This function plays a crucial role in ensuring that any changes made within the context are rolled back and that all associated resources are properly cleaned up, providing a reliable and consistent state after exiting the 'with' block. 

**Note**: The **__exit__** function is automatically called when exiting the 'with' block and should not be invoked directly. It is responsible for performing cleanup, regardless of whether an exception occurred or not.
***
### FunctionDef after_flush(self, db, flush_context, instances)
**after_flush**: The function 'after_flush' is triggered after a database flush event and is responsible for tracking the identities of new instances in the database.

**parameters**:
- self: The instance of the 'Restorable' class.
- db: The database connection or session.
- flush_context: Contextual information related to the database flush operation.
- instances (optional): Specific instances to consider; if not provided, all new instances in 'db.new' will be processed.

**Code Description**:
The 'after_flush' function is an integral part of the 'Restorable' class and is designed to work in conjunction with the '__enter__' and '__exit__' methods. Its primary purpose is to capture and record the identities of new instances that are added to the database during a flush operation.

Within the function, it iterates over the 'db.new' collection, which contains instances newly added to the database. For each instance, it extracts the class and identifier using 'util.identity_key()'. The class represents the type of the instance, and the identifier uniquely identifies the instance within its class. These identities are then stored in the 'history' attribute, which is a dictionary where each key is a class, and the corresponding value is a set of identifiers for instances of that class.

This function is called by the '__enter__' method, which sets up an event listener to trigger 'after_flush' after a database flush. The '__exit__' method, on the other hand, performs cleanup operations, including removing the event listener and deleting the instances tracked in the 'history'.

**Note**: The 'after_flush' function plays a crucial role in maintaining a record of new instances added to the database. It ensures that the 'history' attribute is updated accordingly, enabling subsequent actions or rollbacks based on these recorded identities.
***
## ClassDef DBHistory
Doc is waiting to be generated...
### FunctionDef __init__(self, session)
**__init__**: The function **__init__** initializes the DBHistory object and sets up the necessary attributes for tracking database changes.

**parameters**:
- self: A reference to the DBHistory object being initialized.
- session: The database session object. It can be either a Session or a ScopedSession instance.

**Code Description**:
The **__init__** function takes two parameters: self and session. It first asserts that the session parameter is an instance of either Session or ScopedSession, raising an AssertionError if the condition is not met. Then, it assigns the session object to the self.session attribute.

The function then sets the _target attribute to the session object. If the session is a ScopedSession, it retrieves the registry from the session and assigns it to _target instead. This _target attribute seems to be used for internal bookkeeping or event handling, as it provides a reference to the active session or its registry.

Next, the function initializes several sets and dictionaries to track created, deleted, and updated records. The _created, _deleted, and _updated sets seem to store the actual changed records, while the created_idents, updated_idents, and deleted_idents dictionaries likely hold additional information or metadata about the changes.

**Note**:
- The XXX comment in the code indicates that there is some uncertainty about whether events should be triggered on the class or the object. This may require further consideration or clarification.
- The _target attribute is used instead of self.target to avoid potential naming conflicts with the session object's attributes.
- The sets and dictionaries initialized in this function provide a way to track and identify changes made to the database during a session. This information can be used for auditing, undo/redo functionality, or other data management purposes.
***
### FunctionDef last(self, model_cls, mode)
**last**: The function retrieves the set of identifiers for the last created, updated, or deleted instances of a given model class. 

**parameters**: 
- self: The instance of the class. 
- model_cls: The model class for which the last action is being queried. 
- mode: A string indicating the type of action to query, either 'created', 'updated', or 'deleted'. 

**Code Description**: 
The 'last' function is a method of the 'DBHistory' class, which appears to be responsible for tracking and managing the history of changes to database models. When called, it first asserts that the provided 'mode' parameter is one of the three valid options: 'created', 'updated', or 'deleted'. This assertion helps ensure that the function is used correctly and prevents potential errors. 

The function then uses the 'getattr' function to dynamically access an attribute named after the provided 'mode'. For example, if 'mode' is 'created', it will access the 'created_idents' attribute of the instance. These attributes appear to be dictionaries that store sets of identifiers for the corresponding actions. The function retrieves the set of identifiers associated with the given 'model_cls' from this dictionary. 

The 'last' function is then utilized by three other methods: 'last_created', 'last_updated', and 'last_deleted'. These methods call 'last' with the appropriate 'mode' value and then perform additional processing on the returned set of identifiers. For example, 'last_created' and 'last_updated' call the '_idents_to_objects_set' method to further process the identifiers, while 'last_deleted' simply returns the result of the 'last' function directly. 

The 'assert_' method also uses the 'last' function to retrieve the identifiers based on the provided 'mode' and then performs additional checks and assertions to ensure that instances of the model class were modified in the specified way. 

**Note**: 
- The 'last' function relies on the dynamic attribute names ('created_idents', 'updated_idents', 'deleted_idents') being present and correctly set on the instance. 
- The function assumes that the 'model_cls' is a valid key in the corresponding 'idents' dictionary and does not handle cases where it might be missing. 

**Output Example**: 
Assuming the following identifiers have been recorded for a 'User' model class: 

```python
self.created_idents = {
***
### FunctionDef _idents_to_objects_set(self, idents, model_cls)
**_idents_to_objects_set**: The function **_idents_to_objects_set** retrieves a set of objects corresponding to the provided identifiers (**idents**) for a given model class (**model_cls**). 

**Parameters**:
- **idents**: A list or iterable of identifiers (e.g., primary keys) used to uniquely identify objects of the specified model class.
- **model_cls**: The model class for which the objects need to be retrieved.

**Code Description**: This function utilizes the **session.query** method to perform a database query. It constructs a set by executing a query for each identifier in the **idents** list, retrieving the corresponding object of the specified **model_cls**. This allows for efficient retrieval of multiple objects based on their identifiers. 

The **_idents_to_objects_set** function is used by several other methods within the **DBHistory** class:
- **last_created**: Retrieves the last created object of the specified model class by querying the object with the latest 'created' timestamp.
- **last_updated**: Retrieves the last updated object of the specified model class by querying the object with the latest 'updated' timestamp.
- **assert_created**: Retrieves objects of the specified model class to perform assertions on their 'created' status.
- **assert_updated**: Retrieves objects of the specified model class to perform assertions on their 'updated' status.

**Note**: This function assumes that the provided identifiers are valid and exist in the database. Invalid or non-existent identifiers may result in empty entries in the returned set. 

**Output Example**: 
Assuming the following identifiers for the 'User' model class: [1, 2, 3, 4], a possible output of the function call could be: { <
***
### FunctionDef last_created(self, model_cls)
**last_created**: The function retrieves the set of objects corresponding to the last created instances of a given model class. 

**parameters**: 
- self: The instance of the class. 
- model_cls: The model class for which the last created instances are being queried. 

**Code Description**: 
The 'last_created' function is a method within the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function utilizes two other functions: 'last' and '_idents_to_objects_set'. 

Firstly, it calls the 'last' function with the 'model_cls' parameter and the mode set to 'created'. This retrieves the set of identifiers for the last created instances of the specified model class. 

Then, it passes the resulting set of identifiers and the 'model_cls' to the '_idents_to_objects_set' function. This function performs a database query to retrieve the actual objects corresponding to the provided identifiers and model class. 

The 'last_created' function is used in multiple test cases within the 'tests.py' module. These tests verify the expected behavior of the function by asserting the equality of the returned set of objects. For example, in the 'test_models_history_created' and 'test_models_history_created_with_scoped_session' tests, a 'User' object is created and added to the session. The 'last_created' function is then called with the 'User' model class, and the test asserts that the returned set contains the newly created 'user' object. 

**Note**: 
- The 'last_created' function relies on the 'last' function to provide the correct set of identifiers for the given mode and model class. 
- The '_idents_to_objects_set' function assumes that the provided identifiers are valid and exist in the database. Invalid or non-existent identifiers may result in unexpected behavior or errors. 

**Output Example**: 
Assuming the following code snippet: 

```python
with DBHistory(self.session) as history:
    user = User(name='test')
    self.session.add(user)
    self.session.commit()

last_created_users = history.last_created(User)
```

The output of `last_created_users` would be a set containing the 'user' object that was recently created, assuming the 'created_idents' attribute was properly set and the identifier is valid. 

This documentation provides an overview of the 'last_created' function, including its parameters, functionality, related code, and usage examples. It aims to assist developers in understanding and utilizing this function effectively within the context of the 'testalchemy.py' and 'tests.py' modules.
***
### FunctionDef last_updated(self, model_cls)
**last_updated**: The function retrieves the set of objects corresponding to the last updated instances of a given model class. 

**parameters**: 
- self: The instance of the class. 
- model_cls: The model class for which the last updated instances are being queried. 

**Code Description**: 
The 'last_updated' function is a method within the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function utilizes two other functions: 'last' and '_idents_to_objects_set'. 

Firstly, it calls the 'last' function with the 'model_cls' parameter and the 'mode' set to 'updated'. This retrieves the set of identifiers for the last updated instances of the specified model class. 

Then, the '_idents_to_objects_set' function is called with the returned set of identifiers and the 'model_cls' parameter. This function performs a database query to retrieve the corresponding objects for each identifier, resulting in a set of objects that were last updated for the given model class. 

The 'last_updated' function is used in the test suite to verify the expected behavior of the 'DBHistory' class. In the test cases, it is used to assert that the 'DBHistory' object correctly tracks and returns the last updated instances of a 'User' model class. 

**Note**: 
- The 'last_updated' function relies on the 'last' and '_idents_to_objects_set' functions to function correctly. 
- The function assumes that the provided identifiers are valid and exist in the database. Invalid or non-existent identifiers may result in unexpected behavior. 

**Output Example**: 
Assuming the following identifiers have been recorded for a 'User' model class: [user1_id, user2_id], and the corresponding objects are {user1, user2}, a possible output of the function call could be: {user1, user2}, indicating that these are the last updated instances of the 'User' model class.
***
### FunctionDef last_deleted(self, model_cls)
**last_deleted**: The function retrieves the set of identifiers for the last deleted instances of a given model class. 

**parameters**: 
- self: The instance of the class. 
- model_cls: The model class for which the last deleted instances are being queried. 

**Code Description**: 
The 'last_deleted' function is a method within the 'DBHistory' class, designed to track and manage the history of changes to database models, specifically focusing on deleted instances. It utilizes the 'last' function, which is another method within the same class, to retrieve the desired information. 

The 'last' function, when called by 'last_deleted', first performs an assertion check to ensure that the provided 'mode' parameter is set to 'deleted'. This validation step helps prevent potential errors by ensuring the correct usage of the function. 

Then, the 'last' function dynamically accesses the 'deleted_idents' attribute of the instance using the 'getattr' function. This attribute is expected to be a dictionary that stores sets of identifiers associated with deleted instances of the model class. The function retrieves the set of identifiers corresponding to the specified 'model_cls' from this dictionary. 

The 'last_deleted' function serves as a convenient wrapper around the 'last' function, specifically tailored for retrieving information about deleted instances. It simplifies the process by directly calling 'last' with the 'mode' value set to 'deleted' and returning the result without any further processing. 

**Note**: 
- The 'last_deleted' function relies on the presence and correct setup of the 'deleted_idents' dynamic attribute on the instance. 
- It assumes that the 'model_cls' is a valid key in the 'deleted_idents' dictionary and does not handle potential missing key scenarios. 

**Output Example**: 
Assuming a 'User' model class has been deleted, the output of the 'last_deleted' function might look like this: 

```python
history = DBHistory(session)
history.last_deleted(User)
# Output: set([(user_id,), ...])
```

In this example, the 'last_deleted' function is called on the 'history' instance, passing the 'User' model class as an argument. The function returns a set of tuples containing the identifiers of the last deleted 'User' instances.
***
### FunctionDef assert_(self, model_cls, ident, mode)
**assert_****: The function performs assertions to check if instances of a specified model class were created, updated, or deleted, optionally checking for a specific identity.

**parameters**:
- self: The instance of the class.
- model_cls: The model class for which the assertion is being made.
- ident: The specific identity to check for. It can be None, a single value, or a tuple/list of values.
- mode: A string indicating the type of action to assert, either 'created', 'updated', or 'deleted'. The default is 'created'.

**Code Description**:
The 'assert_' function is a method of the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function takes a model class and an optional identity as input and checks if instances of the model class were modified as specified by the 'mode' parameter.

The function first calls the 'last' method to retrieve the set of identifiers for the last created, updated, or deleted instances of the given model class, depending on the 'mode' parameter. It then checks if any identifiers were returned and raises an assertion error if none are found, with an error message indicating that no instances of the model class were modified as expected.

If an 'ident' parameter is provided, the function performs an additional check. It ensures that the given identity is present in the set of identifiers returned by the 'last' method. If the identity is not found, another assertion error is raised, indicating that no instances of the model class with the specified identity were modified as expected.

Finally, the function returns the set of identifiers obtained from the 'last' method.

This function is called by three other methods: 'assert_created', 'assert_updated', and 'assert_deleted'. These methods provide a more specific assertion for each type of action ('created', 'updated', or 'deleted') and perform additional processing on the returned set of identifiers using the '_idents_to_objects_set' method.

**Note**:
- The 'assert_' function relies on the 'last' method to retrieve the correct set of identifiers based on the provided 'mode'.
- The function assumes that the 'model_cls' is a valid key in the corresponding 'idents' dictionary and does not handle potential key errors.

**Output Example**:
Assuming the following identifiers have been recorded for a 'User' model class:

```python
self.created_idents = {
    'user1': ['id1', 'id2'],
    'user2': ['id3', 'id4']
}
self.updated_idents = {
    'user1': ['id5', 'id6']
}
self.deleted_idents = {
    'user2': ['id7']
}
```

Calling 'assert_' with 'model_cls' as 'User' and 'mode' as 'created' would return the set of identifiers: {['id1', 'id2'], ['id3', 'id4']}. If 'ident' is specified as 'user1', the function would assert that 'user1' is present in the returned set of identifiers.
***
### FunctionDef assert_created(self, model_cls, ident)
**assert_created**: The function **assert_created** is used to perform assertions on the 'created' status of instances of a specified model class, with an optional check for a specific identity. 

**Parameters**:
- **self**: The instance of the class.
- **model_cls**: The model class for which the assertion is made. It specifies the type of objects to perform the assertion on.
- **ident**: The specific identity to check for. It can be None (default), a single value, or a tuple/list of values. This parameter is optional.

**Code Description**: The 'assert_created' function is a part of the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function utilizes the 'assert_' and '_idents_to_objects_set' methods to perform its assertions. 

'assert_created' first calls the 'assert_' method with the provided 'model_cls', 'ident', and the mode 'created'. This checks if instances of the specified model class were created and optionally verifies the presence of the given identity in the set of identifiers for the created instances. 

The return value of 'assert_', which is a set of identifiers, is then passed to the '_idents_to_objects_set' method, along with the 'model_cls'. This retrieves a set of objects corresponding to the provided identifiers for the specified model class. 

By combining the 'assert_' and '_idents_to_objects_set' methods, 'assert_created' allows for efficient retrieval and assertion of the 'created' status of objects, with the option to specify a particular identity to check for. 

**Note**: The 'assert_created' function assumes that the provided identifiers are valid and exist in the database. Invalid or non-existent identifiers may lead to unexpected results or errors. 

**Output Example**: 
Assuming the following identifiers for the 'User' model class: [user1, user2, user3], and the 'created' status for these users, a possible output of the function call could be: { <user1: User object with created status>, <user2: User object with created status>, <user3: User object with created status> }

This output represents a set of 'User' objects that have been created, and the function has successfully retrieved and asserted their 'created' status.
***
### FunctionDef assert_updated(self, model_cls, ident)
**assert_updated**: The function **assert_updated** checks if instances of a specified model class have been updated, optionally checking for a specific identity. 

**Parameters**:
- **self**: The instance of the class.
- **model_cls**: The model class for which the assertion is being made.
- **ident**: The specific identity to check for. It can be None (default), a single value, or a tuple/list of values.

**Code Description**: The 'assert_updated' function is a part of the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function utilizes the 'assert_' and '_idents_to_objects_set' methods to perform its task. 

It first calls the 'assert_' function with the provided 'model_cls' and 'ident' parameters, and the 'mode' parameter set to 'updated'. This checks if instances of the specified model class have been updated. The 'assert_' function retrieves the set of identifiers for the last updated instances of the given model class and performs the necessary assertions. 

The 'assert_updated' function then calls the '_idents_to_objects_set' function, passing the result of the 'assert_' function and the 'model_cls' parameter. This retrieves a set of objects corresponding to the provided identifiers for the specified model class. 

This function is used by the 'assert_updated_one' method, which provides a more specific assertion for checking if a single instance of the model class has been updated. 

**Note**: The 'assert_updated' function relies on the 'assert_' and '_idents_to_objects_set' methods to perform its assertions. It assumes that the provided identifiers are valid and exist in the database. Invalid or non-existent identifiers may lead to unexpected results. 

**Output Example**: Assuming the following identifiers for the 'User' model class: [user1, user2, user3], and the 'ident' parameter is set to 'user1', a possible output of the function call could be: [<user1 object>, <user2 object>, <user3 object>], indicating that these instances of the 'User' model class have been updated.
***
### FunctionDef assert_deleted(self, model_cls, ident)
**assert_deleted**: The function checks if instances of a specified model class were deleted, with an optional check for a specific identity. 

**parameters**:
- self: The instance of the class.
- model_cls: The model class for which the deletion assertion is being made.
- ident: The specific identity to check for deletion. It can be None or a single value.

**Code Description**:
The 'assert_deleted' function is a part of the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function is used to verify if instances of a given model class have been deleted. It takes the 'model_cls' and an optional 'ident' parameter. By calling the 'assert_' function with the 'mode' parameter set to 'deleted', it checks if the specified instances have been deleted. 

The 'assert_' function, in turn, retrieves the set of identifiers for the last deleted instances of the given 'model_cls' and performs the necessary assertions. If the 'ident' parameter is provided, it further checks if the given identity is present in the set of deleted identifiers. 

This function is called by 'assert_deleted_one' in the same module, which provides a more specific assertion for a single deletion. It also serves as a helper function for testing purposes in the 'tests.py' module, where it is used to verify the expected behavior of instance deletions. 

**Note**:
- The 'assert_deleted' function relies on the 'assert_' function to perform the actual assertion logic, including the retrieval of identifiers based on the provided 'mode'.
- This function assumes that the 'model_cls' is a valid key and does not handle potential key errors.

**Output Example**:
Assuming the following identifiers have been recorded for a 'User' model class:
```python
self.created_idents = {
    'user1': ['id1', 'id2'],
    'user2': ['id3', 'id4']
}
self.deleted_idents = {
    'user2': ['id7']
}
```

Calling 'assert_deleted' with 'model_cls' as 'User' would return a set of identifiers indicating the deleted instances: {['id7']}. If 'ident' is specified as 'user2', the function would assert that 'user2' is present in the set of deleted identifiers.
***
### FunctionDef assert_one(self, dataset, model_cls, mode)
**assert_one**: The function **assert_one** checks if a dataset contains exactly one instance of a specified model class in a particular mode and returns that instance. 

**parameters**:
- dataset: The collection of data instances to be checked.
- model_cls: The specific model class that is sought within the dataset.
- mode: The mode or state indicating the context of the model class (e.g., 'created', 'deleted', 'updated').

**Code Description**: This function first checks the length of the dataset. If it does not contain exactly one instance (i.e., the length is not equal to 1), an AssertionError is raised, indicating that there should be only one instance of the specified model class in the given mode. The error message includes the actual number of instances found, the name of the model class, and the mode. If the dataset length is as expected, the function returns the single instance by popping it from the dataset, ensuring it is the only one present. 

**Note**: This function is used in conjunction with other assert functions (assert_created, assert_deleted, assert_updated) to verify the presence of specific model class instances in different states. It ensures that exactly one instance exists in the dataset, making it useful for unique instance checks during testing or validation. 

**Output Example**: 
```python
instance = assert_one(dataset, MyModelClass, 'created')
print(instance)
# Output: <__main__.MyModelClass object at 0x...>
```

In this example, assert_one is used to retrieve the single instance of MyModelClass that was created and is present in the dataset. The returned instance can then be used for further assertions or inspections.
***
### FunctionDef assert_created_one(self, model_cls)
**assert_created_one**: The function **assert_created_one** checks if exactly one instance of a specified model class was created and returns that instance. 

**Parameters**:
- **self**: The instance of the class.
- **model_cls**: The model class for which the assertion is made. It specifies the type of objects to check for creation.

**Code Description**: This function is used to assert that only a single instance of a particular model class was created. It combines the functionality of **assert_created** and **assert_one**. 

First, **assert_created** is called with the provided **model_cls** to check if any instances of the specified model class were created. This function performs assertions on the 'created' status of instances, as described in its documentation. 

The result of **assert_created** is then passed to **assert_one**, along with the original **model_cls**. **assert_one** checks if the dataset (in this case, the result of **assert_created**) contains exactly one instance of the specified model class. 

By combining these two functions, **assert_created_one** ensures that only one instance of the specified model class was created and returns that instance. 

**Note**: This function assumes that the provided model class exists and that identifiers are valid. Invalid or non-existent identifiers or model classes may lead to unexpected behavior or errors. 

**Output Example**: 
Assuming the following code snippet:
```python
from testalchemy import DBHistory
from your_app import User

session = ...  # Your database session
with DBHistory(session) as history:
    user = User(name='test')
    session.add(user)
    session.commit()
    created_user = history.assert_created_one(User)
```

The output of **history.assert_created_one(User)** would be the single instance of the **User** model class that was created, which in this case, is the **user** object.
***
### FunctionDef assert_deleted_one(self, model_cls)
**assert_deleted_one**: The function checks if exactly one instance of a specified model class was deleted and returns that instance. 

**parameters**:
- self: The instance of the class.
- model_cls: The model class for which the deletion assertion is being made.

**Code Description**: The 'assert_deleted_one' function is a part of the 'DBHistory' class, which is responsible for tracking and managing the history of changes to database models. This function is used to verify if exactly one instance of a given model class has been deleted and to return that instance. 

It first calls the 'assert_deleted' function, which checks if any instances of the specified model class were deleted. The 'assert_deleted' function is a helper function that utilizes the 'assert_' function to perform the actual assertion logic and retrieve identifiers based on the provided mode ('deleted' in this case). 

Then, the result from 'assert_deleted' is passed to the 'assert_one' function, which checks if the dataset (in this case, the set of deleted identifiers) contains exactly one instance of the specified model class. If there is not exactly one instance, an 'AssertionError' is raised, indicating that there should only be a single instance of the deleted model class. If the condition is met, the function returns that single instance. 

This function is used in the 'tests.py' module to verify the expected behavior of instance deletions. In the test cases, it is used to assert that exactly one instance of a 'User' model class was deleted, and the returned value is compared to the expected outcome. 

**Note**:
- The 'assert_deleted' and 'assert_one' functions, which are called by 'assert_deleted_one', assume that 'model_cls' is a valid key and do not handle potential key errors.
- This function relies on the underlying 'assert_' function for the actual assertion logic, including identifier retrieval based on the provided mode.

**Output Example**: 
Assuming the following identifiers have been recorded for a 'User' model class:
```python
self.created_idents = {
    'user1': ['id1', 'id2'],
    'user2': ['id3', 'id4']
}
self.deleted_idents = {
    'user2': ['id7']
}
```

Calling 'assert_deleted_one' with 'model_cls' as 'User' would return the single deleted instance: ['id7'].
***
### FunctionDef assert_updated_one(self, model_cls)
**assert_updated_one**: The function **assert_updated_one** checks if a single instance of a specified model class has been updated and returns that instance. 

**parameters**:
- **self**: The instance of the class.
- **model_cls**: The model class for which the assertion is being made.

**Code Description**: This function is a part of the 'DBHistory' class and is used to check if exactly one instance of the specified model class has been updated. It first calls the 'assert_updated' function, which checks if any instances of the model class have been updated, and then utilizes the 'assert_one' function to ensure that only one instance has been updated. 

The 'assert_updated' function is responsible for checking the update status of instances by retrieving the set of identifiers for the last updated instances of the given model class. It then performs assertions to confirm if any updates have occurred. 

Subsequently, the 'assert_one' function is invoked to ensure that only one instance of the model class has been updated. It checks the length of the dataset and raises an 'AssertionError' if there is not exactly one instance updated. This provides a specific assertion for unique instance updates. 

**Note**: The 'assert_updated_one' function relies on the 'assert_updated' and 'assert_one' functions to perform its task. It assumes that the identifiers used are valid and exist in the database. Using invalid or non-existent identifiers may lead to unexpected results. 

**Output Example**: Assuming the following identifiers for the 'User' model class: [user1, user2, user3], and an update has occurred for 'user2', a possible output of the function call could be: <user2 object>, indicating that this instance of the 'User' model class has been updated.
***
### FunctionDef assert_nothing_happened(self)
**assert_nothing_happened**: The function **assert_nothing_happened** is used to verify that no database operations, specifically creation, update, or deletion of entities, have taken place within a specific context or test case. 

**parameters**: 
- self: The instance of the DBHistory class, which is expected to have attributes like created_idents, updated_idents, and deleted_idents, representing the database operations that have occurred. 

**Code Description**: This function is typically used in testing scenarios to ensure that certain database operations have not occurred. It checks three conditions: 
1. **Creation Check**: It asserts that self.created_idents is empty, ensuring that no entities have been created. 
2. **Update Check**: It verifies that self.updated_idents is empty, confirming that no updates have been made to existing entities. 
3. **Deletion Check**: The function also checks that self.deleted_idents is empty, indicating that no entities have been deleted. 

If any of these conditions are not met, the function raises an AssertionError with an appropriate error message, indicating which type of operation was detected. 

This function is particularly useful in scenarios where you want to validate the behavior of your code or a specific function, ensuring that it does not perform unintended database operations. For example, in the provided test cases from tests.py, the function is used to verify that: 
1. **test_nothing_happened_does_not_throw_when_nothing_happened**: Running a simple query that retrieves all User entities should not trigger any creation, update, or deletion assertions. 
2. **test_nothing_happened_throws_on_creating**: Adding a new User entity and committing it to the database should cause the assert_nothing_happened function to raise an AssertionError, indicating that something was created. 
3. **test_nothing_happened_throws_on_update**: Similarly, updating the name of an existing User entity and committing the change should result in an AssertionError, as the function detects that an update has occurred. 
4. **test_nothing_happened_throws_on_delete**: Deleting a User entity and committing the deletion should also trigger an AssertionError, signifying that an entity was deleted. 

**Note**: This function specifically targets the created_idents, updated_idents, and deleted_idents attributes of the DBHistory class instance. Ensure that these attributes are properly maintained and updated within the context of your testing or usage to ensure accurate assertions.
***
### FunctionDef clear(self)
**clear**: The function **clear** resets the internal state of the DBHistory class by clearing various identifier dictionaries and invoking the internal clear_cache method.

**parameters**: This function does not take any parameters.

**Code Description**: The **clear** function is responsible for resetting the internal state of the DBHistory class. It operates by first clearing three identifier dictionaries: self.created_idents, self.updated_idents, and self.deleted_idents. These dictionaries likely store information about created, updated, or deleted items, respectively. By clearing these dictionaries, any previously tracked items are removed from the class's memory.

Additionally, the **clear** function invokes another internal method, **clear_cache**, which further contributes to resetting the class's state. The **clear_cache** method is responsible for resetting three internal sets (_created, _updated, and _deleted) that are likely used for tracking similar operations.

This function is typically called to reset the state of the DBHistory class after performing a series of operations or when entering or exiting a new context. It ensures that any previous data or state does not impact subsequent operations, providing a fresh starting point for the class.

**Note**: The **clear** function is an important tool for managing the state of the DBHistory class. It should be used carefully, as it will remove all previously tracked information. This function is likely to be invoked automatically by other methods within the class or when a clean starting state is required.
***
### FunctionDef clear_cache(self)
**clear_cache**: The function **clear_cache** resets the internal sets that track created, updated, and deleted items.

**parameters**: This function does not take any parameters.

**Code Description**: The **clear_cache** function is used to clear the internal state of the DBHistory class by resetting three sets: _created, _updated, and _deleted. These sets are likely used to track the status of certain items, and clearing them ensures that the class starts with a fresh state.

This function is called by multiple methods within the DBHistory class:
1. **clear**: The clear method invokes clear_cache, likely to reset the state after performing other operations.
2. **__enter__**: The context manager's __enter__ method sets up event listeners and then calls clear_cache, possibly to ensure that any previous state is cleared before entering a new context.
3. **__exit__**: Similarly, the __exit__ method of the context manager removes the event listeners and then calls clear_cache to reset the state after exiting the context.
4. **_after_commit**: The _after_commit method is triggered after a commit and populates ident dictionaries before invoking clear_cache to reset the state.
5. **_after_rollback**: The _after_rollback method is called after a rollback and immediately clears the cache.

**Note**: The clear_cache function is an internal method used to manage the state of the DBHistory class. It is automatically invoked by other methods within the class to ensure proper tracking and handling of created, updated, and deleted items.
***
### FunctionDef __enter__(self)
Doc is waiting to be generated...
***
### FunctionDef __exit__(self, type, value, traceback)
Doc is waiting to be generated...
***
### FunctionDef _populate_idents_dict(self, idents, objects)
**_populate_idents_dict**: The function **_populate_idents_dict** is responsible for populating the identity dictionary with object identifiers.

**parameters**:
- idents: The first parameter is expected to be a dictionary that will be used to store the object identifiers.
- objects: The second parameter is a list or iterable of objects for which the identifiers need to be generated and populated into the idents dictionary.

**Code Description**: This function, **_populate_idents_dict**, is an essential utility function within the DBHistory class. It is used to facilitate the management of object identities and their associated keys. The function takes a list of objects and a dictionary as arguments and iterates over the objects to generate their unique identifiers. These identifiers are then used to populate the idents dictionary.

The function utilizes the util.identity_key function to generate the unique identifier for each object. The resulting identifier is a tuple with two elements. The idents dictionary is then updated using the setdefault method, which ensures that there is a set associated with the first element of the identifier tuple. The second element of the identifier tuple is then added to this set.

This function is called by the _after_commit method of the same class. _after_commit is responsible for handling the after-commit behavior of a database transaction. In this method, **_populate_idents_dict** is used to populate the created_idents, updated_idents, and deleted_idents dictionaries with the respective object identifiers. This separation allows for efficient tracking of created, updated, and deleted objects during a database transaction.

**Note**: The _populate_idents_dict function plays a crucial role in maintaining the integrity of object identities within the DBHistory class. It ensures that the idents dictionary is accurately populated, enabling efficient tracking and management of objects and their associated identifiers.
***
### FunctionDef _after_flush(self, db, flush_context, instances)
Doc is waiting to be generated...
#### FunctionDef identityset_to_set(obj)
**identityset_to_set**: The function transforms the internal _members attribute of an object into a set.

**parameters**:
- obj: The function takes a single parameter, obj, which represents an instance of a class.

**Code Description**: This function, identityset_to_set, operates on the internal attribute _members of the provided object. It extracts the values stored in _members, which are assumed to be unique, and converts them into a standard set data structure. This transformation allows for efficient storage and retrieval of unique values associated with the object.

The function is named identityset_to_set because it creates a set that represents the identity of the object based on its _members values. The use of the term "identity" suggests that the set created uniquely identifies the object or a particular aspect of it.

**Note**: The function relies on the presence and structure of the _members attribute within the provided object. Ensure that the obj parameter has the expected _members attribute with the appropriate values before using this function.

**Output Example**: Let's say the obj parameter is an instance of a class with the following _members attribute:

```python
_members = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}
```

When identityset_to_set is called with this obj parameter, it will return:

```python
{'value1', 'value2', 'value3'}
```

The function has transformed the values ('value1', 'value2', 'value3') from the _members dictionary into a set, discarding the keys ('key1', 'key2', 'key3'). This output represents a unique collection of values associated with the object.
***
***
### FunctionDef _after_commit(self, db)
**_after_commit**: The function **_after_commit** is triggered after a database commit and is responsible for populating identity dictionaries and managing the internal state of the DBHistory class. 

**parameters**:
- self: A common parameter in Python methods, referring to the instance of the class. 
- db: The database connection or transaction context. 

**Code Description**: The **_after_commit** function plays a crucial role in maintaining the integrity of object identities within the DBHistory class, specifically after a database commit operation. 

Firstly, the function checks if the db.transaction is nested. If it is, the function returns without executing the remaining code. This is because, in nested transactions, the 'after_commit' event is unexpectedly triggered during the _flush operation, and the function avoids performing any actions in this case. 

Next, the function proceeds to populate three identity dictionaries: created_idents, updated_idents, and deleted_idents. It achieves this by calling the _populate_idents_dict function three times, passing the respective dictionary and a list of objects (_created, _updated, or _deleted) as arguments. The _populate_idents_dict function generates unique identifiers for each object and populates the corresponding dictionary. 

After populating the identity dictionaries, the _after_commit function invokes the clear_cache method. This step resets the internal sets that track created, updated, and deleted items, ensuring the DBHistory class starts with a fresh state after the commit operation. 

This function is an important part of the DBHistory class's event-listening mechanism. It is called by the __enter__ method of the same class, which sets up event listeners for 'after_flush', 'after_commit', and 'after_soft_rollback' events. The __enter__ method then invokes _after_commit, ensuring that any previous state is cleared before entering a new context. 

Similarly, the __exit__ method of the DBHistory class removes the event listeners and calls _after_commit to reset the state after exiting the context. This ensures that the internal state of the DBHistory class is managed appropriately, and any changes made during the context are properly reflected or rolled back. 

**Note**: The _after_commit function is an internal method used to manage the state of the DBHistory class, specifically after a database commit. It is automatically invoked by the __enter__ and __exit__ methods to ensure the proper tracking and handling of created, updated, and deleted items within the class. 

**Output Example**: 
None. This function does not return any value. Its purpose is to perform necessary operations after a database commit to maintain the integrity of object identities and manage the internal state of the DBHistory class.
***
### FunctionDef _after_rollback(self, db, prev_tx)
Doc is waiting to be generated...
***
