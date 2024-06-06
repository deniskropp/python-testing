## ClassDef sample_property
**sample_property**: The function of sample_property is to dynamically create properties on an instance of a class.

**Attributes**:

* `method`: The method to be called when the property is accessed or set.
* `name` (optional): The name of the property, which defaults to the name of the method if not provided.

**Code Description**: This class is designed to dynamically create properties on an instance of a class. When an instance of this class is created, it takes in a method and an optional name as parameters. The method is used to retrieve or set the value of the property, and the name is used to identify the property. If no name is provided, the name of the method is used.

When the property is accessed, the `__get__` method is called with the instance and class as arguments. This method calls the original method with the instance as an argument and returns the result. If the result is a list or tuple, it adds all elements to the database using the `add_all` method. Otherwise, it adds the result to the database using the `add` method.

When the property is set, the `__set__` method is called with the instance and value as arguments. This method calls the original method with the instance and value as arguments and returns the result.

**Note**: The `sample_property` class can be used to dynamically create properties on an instance of a class. It provides a flexible way to add custom behavior to instances of classes without modifying the underlying class definition.

**Output Example**: If we create an instance of this class with a method that returns a list, and then access the property, it will add all elements in the list to the database:
```python
class SampleProperty(sample_property):
    def __init__(self, method):
        super().__init__(method)

    def method(self):
        return [1, 2, 3]

sample = SampleProperty(SampleProperty.method)
sample.property_name = 'my_property'
print(sample.my_property)  # Output: [1, 2, 3]
```
### FunctionDef __init__(self, method, name)
**__init__**: The function of __init__ is responsible for initializing an instance of the class by assigning values to its attributes.

**Parameters**:

* **method**: This parameter represents the method that will be used to initialize the instance.
* **name** (optional): This parameter specifies a custom name for the instance. If not provided, it defaults to the name of the method.

**Code Description**:
The __init__ function takes two parameters: `method` and `name`. The `method` parameter is required and represents the method that will be used to initialize the instance. The `name` parameter is optional and defaults to the name of the method if not provided. Within the function, the `self.method` attribute is assigned the value of the `method` parameter, while the `self.__doc__` attribute is set to the docstring of the `method`. Additionally, the `self.name` attribute is set to the value of the `name` parameter or the name of the method if no custom name was provided.

**Note**: The __init__ function plays a crucial role in initializing instances of the class. It ensures that each instance has a unique identity and provides a way to customize the instance's attributes.
***
### FunctionDef __get__(self, inst, cls)
**__get__**: The function of __get__ is responsible for retrieving the value associated with an instance of a class.

**Parameters**:

· `self`: An instance of the class that defines this method.
· `inst`: The instance being retrieved, which can be None if the retrieval is done through the class itself.
· `cls`: The class definition of the instance being retrieved.

**Code Description**: This function is called when an attribute access operation is performed on an instance of a class. It returns the value associated with that instance or adds it to the instance's database and sets it as an attribute if necessary.

When `inst` is None, the method returns itself, indicating that this is a class-level property. Otherwise, it calls the `method` function with `inst` as an argument, which retrieves the desired value. If the result is a list or tuple, it adds all elements to the instance's database using the `add_all` method. If the result is not a collection, it adds it to the instance's database using the `add` method.

The function also updates the instance's `used_properties` set by adding the name of this property and sets the attribute on the instance using `setattr`. Finally, it returns the retrieved value.

**Note**: This function is part of a larger mechanism for managing properties in an object-oriented system. It is designed to work seamlessly with other functions that define how properties are retrieved and stored.

**Output Example**: Suppose we have a class `Person` with a property `name`, which is defined as follows:
```python
class Person:
    def __init__(self):
        self.db = {}

    @property
    def name(self):
        return "John"

    @name.getter
    def _get_name(self, inst, cls):
        # implementation of the __get__ method
        pass

p = Person()
print(p.name)  # Output: John
```
In this example, when we access `p.name`, the `_get_name` function is called with `inst=p` and `cls=Person`. The function retrieves the value "John" from the instance's database and sets it as an attribute on the instance.
***
### FunctionDef __call__(self, obj)
**__call__**: The function of __call__ is to invoke the method associated with the object.

**Parameters**:

* **obj**: The object to be processed by the method.

**Code Description**: This function is designed to dynamically bind the method to an object, allowing it to be called as a function. When invoked, it returns the result of calling the method on the provided object.

When this function is executed, it takes in an object as input and passes it to the `method` attribute associated with the current instance. The returned value is the result of executing the `method` with the provided object as its argument.

**Note**: This function is typically used in situations where the method needs to be called dynamically or when the object's behavior needs to be customized at runtime.

**Output Example**: Suppose we have an object `obj` and a method `my_method` associated with it. When we call `__call__(obj)`, the output would be the result of executing `my_method(obj)`. For example:
```
result = __call__(obj)
print(result)  # Output: The result of my_method(obj)
```
***
## ClassDef Sample
**Sample**: The function of Sample is a class that provides a mechanism to create instances of a database-backed model.

**Attributes**:

* `db`: An instance of a database connection or registry.
* `used_properties`: A set of properties that have been used in the creation process.
* `__dict__`: A dictionary containing the instance's attributes.

**Code Description**: The Sample class is designed to create instances of a database-backed model. It uses metaclasses to automatically decorate methods and properties with additional functionality. When an instance of Sample is created, it initializes the `db` attribute and sets up the `used_properties` set. The `__init__` method also updates the instance's attributes using the provided keyword arguments.

The class has a special method called `create_all`, which is responsible for creating all instances of properties defined in the class. This method uses the `map` function to iterate over the directory of the class and calls each property as a method, passing the instance as an argument.

**Note**: The Sample class relies on the presence of a `ScopedSession` object or registry in the `db` attribute. If no such object is provided, it will attempt to create one using the `registry()` method.

**Output Example**: When creating an instance of Sample, you can pass keyword arguments to initialize the instance's attributes. For example:
```python
sample = Sample(db=ScopedSession(), name='John', age=30)
```
This would create a new instance of Sample with the given name and age, using the provided database connection.

In the context of the project, the Sample class is used as a base class for other classes that need to interact with a database. It provides a flexible way to define properties and methods that can be used to create and manipulate data in the database.
### ClassDef __metaclass__
**__metaclass__**: The function of __metaclass__ is to modify and transform class attributes.

**Attributes**:

* cls: The current metaclass being instantiated.
* cls_name: The name of the class being defined.
* bases: A tuple of base classes for the new class.
* attributes: A dictionary of attributes for the new class.

**Code Description**: This metaclass is designed to intercept and manipulate the creation of a class. It overrides the `__new__` method, which is responsible for creating a new class object. The `__new__` method takes three parameters: cls (the current metaclass), cls_name (the name of the class being defined), and attributes (a dictionary of attributes for the new class).

The code iterates over the attributes of the newly created class and checks if each attribute is an instance method, a property, or a special attribute. If it is, it wraps the attribute with a custom wrapper to transform its behavior.

**Note**: This metaclass is designed to work in conjunction with other classes that define properties and methods. It is intended for use in specific contexts where class attributes need to be modified or transformed during the creation of a new class.

**Output Example**: The output of this metaclass will be a new class object with modified attributes, which can then be used as a blueprint for creating instances.
#### FunctionDef __new__(cls, cls_name, bases, attributes)
**__new__**: The function of __new__ is responsible for creating a new instance of a class.

**Parameters**:

* `cls`: The class being instantiated.
* `cls_name`: The name of the class being instantiated.
* `bases`: A tuple of base classes for the new class.
* `attributes`: A dictionary of attributes to be set on the new class.

**Code Description**: This function is responsible for creating a new instance of a class. It takes in the class being instantiated, its name, its base classes, and a dictionary of attributes. The function creates a new instance using the `type.__new__` method and then iterates over the attributes of the new instance. For each attribute that starts with an underscore or is named 'create_all', it skips processing. If the attribute is a method type, it gets the underlying function from the method object. If the attribute is a sample property, it checks if the name of the property matches the name of the attribute; if not, it sets the new value as the method of the sample property. Finally, the function returns the newly created instance.

**Note**: This function is part of the metaclass mechanism in Python and is responsible for creating instances of classes. It provides a way to customize the creation process by allowing developers to set attributes on the new instance.

**Output Example**: The output of this function is an instance of the class being instantiated, with its attributes set according to the input parameters.
***
***
### FunctionDef __init__(self, db)
**__init__**: The function of __init__ is responsible for initializing an instance of this class by setting its attributes.

**Parameters**:

* **db**: This parameter represents the database connection or registry.
* **kwargs**: This parameter allows for additional keyword arguments to be passed and set as instance variables.

**Code Description**:
The __init__ function begins by checking if the provided `db` is an instance of `ScopedSession`. If it is, the `db` attribute is updated to reference the registry returned by calling the `registry()` method on the `ScopedSession` object. This ensures that the database connection is properly initialized.

Next, the `used_properties` set is initialized as an empty set, which will be used to keep track of properties that have been accessed or modified during the instance's lifetime.

Finally, the `__dict__` attribute of the instance is updated with the provided keyword arguments (`kwargs`). This allows for flexible initialization of the instance by passing in arbitrary key-value pairs.

**Note**: The `db` parameter is a required argument, and it is recommended to provide a valid database connection or registry. The `kwargs` parameter can be used to pass additional configuration options or data to the instance.
***
### FunctionDef create_all(self)
**create_all**: The function of create_all is responsible for executing all methods defined within an instance of the Sample class.

**Parameters**: None

**Code Description**: This function iterates over the attributes of the instance using the dir() method, and executes each attribute as if it were a method. If the autocommit flag is set to True, the database connection begins with a transaction before executing the methods, and commits after all methods have been executed.

The code demonstrates a flexible approach to object creation, allowing for dynamic execution of arbitrary methods within an instance. This functionality can be useful in scenarios where the specific methods to be executed are not known beforehand or need to be dynamically determined at runtime.

In the context of the project, this function is called by various test cases to verify the correct behavior of the Sample class and its derived classes. The tests demonstrate how the create_all method interacts with the database and populates it with data.

**Note**: When using the create_all method, it is essential to ensure that the autocommit flag is set correctly to avoid unintended side effects on the database. Additionally, the function assumes that all methods executed within an instance are valid and do not raise any exceptions.
***
## ClassDef Restorable
**Restorable**: The function of Restorable is to manage database operations by providing a context manager that ensures proper commit and rollback of changes made during its usage.

**Attributes**:

* `db`: The database object used for storing and retrieving data.
* `watch`: An optional parameter that specifies the watchable object, defaulting to the `db` attribute if not provided.
* `history`: A dictionary that stores the history of changes made during the execution of the context manager.

**Code Description**: The Restorable class is designed as a context manager, allowing it to be used with the `with` statement in Python. When initialized, it sets up the database connection and initializes the `watch` attribute if provided. The `__enter__` method starts listening for events on the watchable object, while the `__exit__` method rolls back any changes made during the execution of the context manager.

When an exception occurs within the context manager, the `__exit__` method is called, which ensures that any pending changes are rolled back and the database connection is closed. The `after_flush` method is called after each flush operation on the watchable object, updating the `history` dictionary with the affected objects.

**Note**: When using Restorable, it is essential to ensure that the `db` attribute is a valid database object, and the `watch` attribute is set correctly if necessary. Additionally, any changes made within the context manager will be rolled back in case of an exception, so it's crucial to commit or rollback explicitly when needed.

In the project, Restorable is used as a utility class to manage database operations in a controlled manner. It provides a way to ensure that changes are properly committed or rolled back, even in the presence of exceptions. The context manager pattern allows for easy integration with other parts of the codebase, making it a versatile tool for managing database interactions.
### FunctionDef __init__(self, db, watch)
**__init__**: The function of __init__ is responsible for initializing an instance of the Restorable class.

**Parameters**:

* **db**: The database connection to be used by the instance.
* **watch** (optional): A watchable database object, which defaults to the db parameter if not provided.

**Code Description**:
The __init__ function initializes a new instance of the Restorable class. It takes two parameters: db and watch. If the db parameter is an instance of ScopedSession, it is converted to its registry equivalent. The self.db attribute is set to the provided db object, and the self.watch attribute is set to either the provided watch object or the db object if no watch object was provided. Additionally, a dictionary called self.history is initialized with an empty state.

**Note**: The __init__ function plays a crucial role in setting up the instance of the Restorable class for further use. It ensures that the instance has a valid database connection and provides a default watchable database object if one is not explicitly provided.
***
### FunctionDef __enter__(self)
**__enter__**: The function of __enter__ is to establish event listening for the 'after_flush' event.

The `__enter__` method listens for the 'after_flush' event and calls the `after_flush` function when triggered.

**Parameters**: None

**Code Description**: This method initializes the instance's behavior by setting up an event listener for the 'after_flush' event. When this event is triggered, it will call the `after_flush` function to handle the event.

The relationship between `__enter__` and its callees in the project is that it sets up the necessary infrastructure for tracking changes made to instances during a database flush operation. The `after_flush` function is responsible for updating the history dictionary with newly added instances, which is used by other parts of the codebase to manage instance state.

**Note**: This method assumes that the event listener mechanism and the `after_flush` function are properly implemented and available for use.
***
### FunctionDef __exit__(self, type, value, traceback)
**__exit__**: The function of __exit__ is responsible for cleaning up resources and performing necessary operations when exiting the context manager.

**Parameters**:

* `self`: an instance of the class
* `type`, `value`, `traceback`: parameters passed from the try-except block

**Code Description**:
The __exit__ method is called when the context manager is exited, typically after a database operation has been performed. It ensures that any pending changes are committed or rolled back, and that resources are released.

Upon entry into this method, it retrieves the associated database object (`db`) and rolls back any outstanding transactions using `db.rollback()`. The `expunge_all()` method is then called to remove all instances from the session cache. The `autoflush` attribute of the database is temporarily set to `False` to prevent automatic flushing.

The method then checks if the database is in autocommit mode (`db.autocommit`). If it is, a new transaction is started using `db.begin()`.

Next, the method iterates over the history dictionary (`self.history`) and deletes any instances that were previously added during a flush operation. This is done by querying the database for each class-identity pair in the history dictionary, retrieving the corresponding instance, and deleting it if it exists.

After cleaning up instances, the method commits the transaction using `db.commit()`, closes the database connection using `db.close()`, and finally restores the original value of `autoflush` to its previous state.

**Note**: The __exit__ method assumes that the database object has a `rollback()` and `expunge_all()` method, as well as an `autoflush` attribute. It also relies on the presence of a history dictionary (`self.history`) to keep track of instances added during flush operations.
***
### FunctionDef after_flush(self, db, flush_context, instances)
**after_flush**: The function of after_flush is to track changes made to instances during a database flush operation.

**Parameters**:

* `self`: an instance of the class
* `db`: the database object
* `flush_context`: the context of the flush operation
* `instances`: an optional parameter, defaulting to None

**Code Description**: The `after_flush` function is called after a database flush operation has been completed. It iterates over the instances that were newly added to the database during the flush operation and updates the history dictionary with their class and identity keys.

The function uses the `util.identity_key` function to extract the class and identity of each instance from the `db.new` collection, which contains the new instances added during the flush operation. The `history` attribute is a dictionary that maps classes to sets of identities, and this function updates it with the newly added instances.

The relationship between `after_flush` and its callers in the project is as follows: `__enter__` method of the `Restorable` class listens for the `after_flush` event and calls this function when the event is triggered. The `__exit__` method of the same class also uses the history dictionary to clean up instances that were previously added during a flush operation.

**Note**: The `after_flush` function assumes that the `db` object has a `new` attribute containing the new instances added during the flush operation, and that the `util.identity_key` function is available for extracting class and identity information from instances.
***
## ClassDef DBHistory
**DBHistory**: The DBHistory class is designed to track changes made to database objects during a session.

**Attributes**:

* `session`: The database session object.
* `_target`: The target of the history tracking (either a scoped session or a regular session).
* `created_idents`, `updated_idents`, and `deleted_ids`: Sets of identifiers for created, updated, and deleted objects respectively.
* `created_idents_dict`, `updated_idents_dict`, and `deleted_idents_dict`: Dictionaries mapping model classes to sets of identifiers for created, updated, and deleted objects respectively.

**Code Description**: The DBHistory class is designed to track changes made to database objects during a session. It provides methods to query the history of changes made to specific models, as well as assertions to verify that certain events have occurred.

When an instance of DBHistory is created, it sets up event listeners for the target session to capture changes made to the database. The `_after_flush`, `_after_commit`, and `_after_rollback` methods are called when the session is flushed, committed, or rolled back respectively. These methods update the internal state of the DBHistory object based on the changes made to the database.

The `last` method returns a set of identifiers for objects that were created, updated, or deleted during the current session. The `_idents_to_objects_set` method converts a set of identifiers into a set of objects.

The `assert_`, `assert_created_`, `assert_updated`, and `assert_deleted` methods raise an AssertionError if no objects have been created, updated, or deleted respectively. The `assert_one` method raises an AssertionError if more than one object has been created, updated, or deleted.

The `clear` and `clear_cache` methods reset the internal state of the DBHistory object to its initial state.

**Note**: The DBHistory class is designed to be used in conjunction with a database session. It assumes that the session is already set up and configured before creating an instance of DBHistory.

**Output Example**:

```
db_history = DBHistory(session)
assert db_history.last(User) == {user1, user2}  # returns a set of identifiers for User objects created during the current session
```
### FunctionDef __init__(self, session)
**__init__**: The function of __init__ is responsible for initializing an instance of the class by setting up essential attributes.

**Parameters**:

* **session**: An instance of either Session or ScopedSession, which represents the database session to be used.

**Code Description**:
The __init__ method begins by asserting that the provided session is an instance of either Session or ScopedSession. This ensures that the session object meets the expected type requirements for this class.

Next, it sets the `self.session` attribute to the provided session object. If the session is an instance of ScopedSession, it further sets the `_target` attribute to the registry returned by the session's `registry()` method. This suggests that the `_target` attribute may be used to access the underlying database or storage mechanism.

The method then initializes three sets: `_created`, `_deleted`, and `_updated`, which are likely used to track changes made to the data during the lifetime of this instance. Additionally, it initializes three dictionaries: `created_idents`, `updated_idents`, and `deleted_idents`, which may be used to store identifiers or keys corresponding to created, updated, and deleted items.

**Note**: The purpose of these sets and dictionaries is not explicitly stated in the code, but they appear to be designed for tracking changes made to the data. It is essential to understand their intended use when working with this class.
***
### FunctionDef last(self, model_cls, mode)
**last**: The function **last** retrieves a set of identifiers for a given model class based on a specified mode.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.
* `mode`: A string indicating the type of operation, which can be either 'created', 'updated', or 'deleted'.

**Code Description**: This function uses an assertion to ensure that the provided mode is one of the allowed values. It then returns a set of identifiers obtained by calling a method on the object, using the specified mode as part of the method name.

From a functional perspective, this function is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this `last` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the given mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class. For example:
```python
{1, 2, 3}  # Set of created instance identifiers
```
***
### FunctionDef _idents_to_objects_set(self, idents, model_cls)
**_idents_to_objects_set**: The function _idents_to_objects_set retrieves a set of objects from the database based on a list of identifiers.

**Parameters**:

* `idents`: A list of identifiers to be retrieved.
* `model_cls`: The class of the model objects to be retrieved.

**Code Description**: This function uses the session query object to retrieve a set of objects from the database. It iterates over the list of identifiers and queries the database for each identifier, returning a set of objects.

The function is called by several other functions in the project, including `last_created`, `last_updated`, `assert_created`, and `assert_updated`. These functions use _idents_to_objects_set to retrieve sets of objects based on their creation or update timestamps. For example, `last_created` retrieves the most recently created objects for a given model class.

**Note**: The function assumes that the identifiers are valid and correspond to existing objects in the database. If an identifier is not found, it will raise an error.

**Output Example**: A possible output of this function could be a set of objects, such as:
```python
{<Object1>, <Object2>, <Object3>}
```
This set contains the objects corresponding to the identifiers provided in the input list.
***
### FunctionDef last_created(self, model_cls)
**last_created**: The function **last_created** retrieves a set of identifiers for a given model class based on the 'created' mode.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.

**Code Description**: This function uses an assertion to ensure that the provided mode is one of the allowed values ('created', 'updated', or 'deleted'). It then returns a set of identifiers obtained by calling another method on the object, using the specified mode as part of the method name. The returned set of identifiers may be empty if no instances of the specified model class match the given mode.

From a functional perspective, this function is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this `last` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The caller is responsible for ensuring that the provided mode is one of the allowed values. If an invalid mode is provided, the function will raise an assertion error.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class, such as `{1, 2, 3}` (a set of created instance identifiers).
***
### FunctionDef last_updated(self, model_cls)
**last_updated**: The function **last_updated** retrieves a set of identifiers for a given model class based on the 'updated' mode.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.

**Code Description**: This function uses an assertion to ensure that the provided mode is one of the allowed values. It then returns a set of identifiers obtained by calling a method on the object, using the specified mode as part of the method name.

The **last_updated** function is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this `last` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the given mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class, such as `{1, 2, 3}` (a set of updated instance identifiers).

The **last_updated** function plays a crucial role in retrieving and processing data related to the 'updated' mode for a given model class. Its functionality is essential for various use cases, including data analysis, reporting, and visualization.
***
### FunctionDef last_deleted(self, model_cls)
**last_deleted**: The function **last_deleted** retrieves the identifiers of instances that have been deleted based on a specified model class.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the deleted identifiers.

**Code Description**: This function calls another method, **last**, with the mode 'deleted' as an argument. The **last** method retrieves a set of identifiers for a given model class based on a specified mode. In this case, it returns a set of identifiers obtained by calling a method on the object, using the 'deleted' mode as part of the method name.

From a functional perspective, this function is called by other objects in the project to retrieve the relevant deleted identifiers for a given model class. For example, **last_created**, **last_updated**, and **last_deleted** functions are all wrappers around this **last** function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the 'deleted' mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the deleted instances of the model class, such as `{1, 2, 3}`.
***
### FunctionDef assert_(self, model_cls, ident, mode)
**assert_**: The function **assert_** is used to verify the existence of instances of a given model class based on a specified mode.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.
* `ident`: An optional identifier to filter the results by. Can be a single value or a tuple/list of values.
* `mode`: A string indicating the type of operation, which can be either 'created', 'updated', or 'deleted'.

**Code Description**: This function first calls the `last` method to retrieve a set of identifiers for the specified model class and mode. It then asserts that the set is not empty using an error message that includes the model class and mode. If an identifier is provided, it checks if the identifier exists in the set of retrieved identifiers. The function returns the set of identifiers.

From a functional perspective, **assert_** is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this `assert_` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the given mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class, such as `{1, 2, 3}` (a set of created instance identifiers).
***
### FunctionDef assert_created(self, model_cls, ident)
**assert_created**: The function **assert_created** is used to verify the existence of instances of a given model class based on their creation timestamp.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.
* `ident` (optional): An optional identifier to filter the results by. Can be a single value or a tuple/list of values.
* `mode` (default: 'created'): A string indicating the type of operation, which can be either 'created', 'updated', or 'deleted'.

**Code Description**: This function first calls the `_idents_to_objects_set` method to retrieve a set of identifiers for the specified model class and mode. It then asserts that the set is not empty using an error message that includes the model class and mode. If an identifier is provided, it checks if the identifier exists in the set of retrieved identifiers.

From a functional perspective, **assert_** is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this `assert_` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the given mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class, such as `{1, 2, 3}` (a set of created instance identifiers).

This function is used in various test cases to verify the correctness of the database history tracking mechanism. For example, `test_models_history_init` and `test_models_history_created` tests use this function to assert that the correct instances are being tracked for a given model class.

In summary, **assert_** is a utility function that provides a way to retrieve and verify the existence of instances based on their creation timestamp, making it an essential component in the project's database history tracking mechanism.
***
### FunctionDef assert_updated(self, model_cls, ident)
**assert_updated**: The function **assert_updated** is used to verify the existence of updated instances of a given model class.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.
* `ident` (optional): An optional identifier to filter the results by. Can be a single value or a tuple/list of values.
* `mode` (default: `'updated'`): A string indicating the type of operation, which can be either `'created'`, `'updated'`, or `'deleted'`.

**Code Description**: This function first calls the `_idents_to_objects_set` method to retrieve a set of identifiers for the specified model class and mode. It then asserts that the set is not empty using an error message that includes the model class and mode. If an identifier is provided, it checks if the identifier exists in the set of retrieved identifiers. The function returns the set of identifiers.

From a functional perspective, **assert_updated** is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this `assert_**` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the given mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class, such as `{1, 2, 3}` (a set of updated instance identifiers).

This function plays a crucial role in the project's data management and querying mechanisms. It provides a way to verify the existence of specific types of instances and retrieve their corresponding identifiers, which can be used for further processing or analysis.
***
### FunctionDef assert_deleted(self, model_cls, ident)
**assert_deleted**: The function **assert_deleted** is used to verify the existence of deleted instances of a given model class.

**Parameters**:

* `model_cls`: The class of the model for which to retrieve the identifiers.
* `ident`: An optional identifier to filter the results by. Can be a single value or a tuple/list of values.

**Code Description**: This function calls the `assert_` method, which retrieves a set of identifiers for the specified model class and mode ('deleted'). It then asserts that the set is not empty using an error message that includes the model class and mode. If an identifier is provided, it checks if the identifier exists in the set of retrieved identifiers.

From a functional perspective, **assert_** is called by other objects in the project to retrieve the relevant identifiers for a given model class. For example, `last_deleted` functions are wrappers around this `assert_` function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The returned set of identifiers may be empty if no instances of the specified model class match the given mode. Additionally, the caller is responsible for ensuring that the provided mode is one of the allowed values.

**Output Example**: A possible return value of this function could be a set of integers or strings representing the identifiers of the relevant instances of the model class, such as `{1, 2, 3}` (a set of deleted instance identifiers).

This function is used in various test cases to verify the correctness of the deletion process. For example, in `test_models_history_deleted`, it is used to check if the deleted identifiers are correctly retrieved and asserted.
***
### FunctionDef assert_one(self, dataset, model_cls, mode)
**assert_one**: The function of assert_one is to verify that the input dataset contains exactly one instance.

**Parameters**:

* `self`: An instance of the class.
* `dataset`: A collection of instances.
* `model_cls`: A class representing the model being tested.
* `mode`: A string indicating the operation mode, which can be 'created', 'updated', or 'deleted'.

**Code Description**: This function checks if the length of the input dataset is equal to 1. If not, it raises an AssertionError with a message indicating that there should only be one instance. Otherwise, it returns the single instance from the dataset by popping it.

In the context of the project, `assert_one` is called by three other functions: `assert_created_one`, `assert_deleted_one`, and `assert_updated_one`. These functions retrieve the result of a database operation (creation, deletion, or update) and pass it to `assert_one` to verify that there is exactly one instance resulting from the operation.

**Note**: The function assumes that the input dataset is not empty. If the dataset is empty, the function will not raise an error but simply return None.

**Output Example**: Suppose the input dataset contains a single instance of a model. The output of `assert_one` would be that instance. For example:
```python
result = assert_one(dataset, model_cls, 'created')
print(result)  # Output: <instance of model_cls>
```
In this example, `assert_one` returns the single instance created by the database operation.
***
### FunctionDef assert_created_one(self, model_cls)
**assert_created_one**: The function **assert_created_one** is used to verify that there is exactly one instance resulting from a database operation.

**Parameters**:

* `self`: An instance of the class.
* `dataset`: A collection of instances.
* `model_cls`: A class representing the model being tested.
* `mode`: A string indicating the operation mode, which can be 'created', 'updated', or 'deleted'.

**Code Description**: This function checks if the length of the input dataset is equal to 1. If not, it raises an AssertionError with a message indicating that there should only be one instance. Otherwise, it returns the single instance from the dataset by popping it.

From a functional perspective, **assert_created_one** is called by other functions in the project to verify the correctness of database operations. For example, `test_models_history_created`, `test_models_history_updated`, and `test_models_history_deleted` tests use this function to assert that the correct instances are being tracked for a given model class.

**Note**: The function assumes that the input dataset is not empty. If the dataset is empty, the function will not raise an error but simply return None.

**Output Example**: Suppose the input dataset contains a single instance of a model. The output of **assert_created_one** would be that instance. For example:

```
result = assert_created_one(dataset, model_cls, 'created')
print(result)  # Output: <instance of model_cls>
```

In this example, **assert_created_one** returns the single instance created by the database operation.

This function is an essential component in the project's database history tracking mechanism, providing a way to verify the existence and uniqueness of instances resulting from database operations.
***
### FunctionDef assert_deleted_one(self, model_cls)
**assert_deleted_one**: The function **assert_deleted_one** is used to verify that there is exactly one instance of a model class after deletion.

**Parameters**:

* `self`: An instance of the class.
* `model_cls`: A class representing the model being tested.
* `mode`: A string indicating the operation mode, which can be 'created', 'updated', or 'deleted'.

**Code Description**: This function calls the **assert_one** method to check if the input dataset contains exactly one instance. If not, it raises an AssertionError with a message indicating that there should only be one instance. Otherwise, it returns the single instance from the dataset by popping it.

From a functional perspective, **assert_deleted_one** is called by other objects in the project to verify the correctness of deletion operations. For example, in the test cases for model history, this function is used to check if the deleted identifiers are correctly retrieved and asserted.

**Note**: The caller is responsible for ensuring that the provided mode is one of the allowed values. Additionally, the returned set of identifiers may be empty if no instances of the specified model class match the given mode.

**Output Example**: A possible return value of this function could be a single instance of the model class, such as an object of type `User`.

This documentation aims to provide a clear and concise understanding of the **assert_deleted_one** function, its parameters, and its behavior. It also highlights the functional perspective of this function in the project and provides notes on its usage.
***
### FunctionDef assert_updated_one(self, model_cls)
**assert_updated_one**: The function **assert_updated_one** is used to verify that there is exactly one instance of a given model class.

**Parameters**:

* `self`: An instance of the class.
* `dataset`: A collection of instances.
* `model_cls`: A class representing the model being tested.
* `mode`: A string indicating the operation mode, which can be 'created', 'updated', or 'deleted'.

**Code Description**: This function checks if the length of the input dataset is equal to 1. If not, it raises an AssertionError with a message indicating that there should only be one instance. Otherwise, it returns the single instance from the dataset by popping it.

From a functional perspective, **assert_updated_one** is called by other objects in the project to verify that there is exactly one instance resulting from a database operation. For example, `last_created`, `last_updated`, and `last_deleted` functions are all wrappers around this function, which provide additional functionality to convert the retrieved identifiers into sets of objects.

**Note**: The function assumes that the input dataset is not empty. If the dataset is empty, the function will not raise an error but simply return None.

**Output Example**: Suppose the input dataset contains a single instance of a model. The output of **assert_updated_one** would be that instance. For example:

```
result = assert_updated_one(dataset, model_cls, 'created')
print(result)  # Output: <instance of model_cls>
```

In this example, **assert_updated_one** returns the single instance created by the database operation.

This function plays a crucial role in the project's data management and querying mechanisms. It provides a way to verify the existence of specific types of instances and retrieve their corresponding identifiers, which can be used for further processing or analysis.
***
### FunctionDef assert_nothing_happened(self)
**assert_nothing_happened**: The function of assert_nothing_happened is to verify that no changes have been made to the database.

**Parameters**: None

**Code Description**: This function asserts that three conditions are met: `created_idents` is empty, `updated_idents` is empty, and `deleted_ids` is empty. If any of these conditions fail, an AssertionError is raised with a message indicating what has changed (i.e., something was created, updated, or deleted).

This function is used in the project to ensure that no unintended changes have been made to the database during certain operations. It is called by several test cases in the `tests.py` module to verify that the expected behavior occurs when creating, updating, and deleting data.

In the context of these tests, `assert_nothing_happened` is used to check that the function under test does not raise an AssertionError when no changes are made. When a change is made (e.g., an object is created, updated, or deleted), the assertion fails, indicating that something has changed as expected.

**Note**: This function should only be called after a database operation has been performed, and it assumes that the `created_idents`, `updated_idents`, and `deleted_ids` attributes have been populated accordingly.
***
### FunctionDef clear(self)
**clear**: The function of clear is to reset the internal state of the object by clearing the created, updated, and deleted identifiers.

**Parameters**: None

**Code Description**: This function resets the `created_idents`, `updated_idents`, and `deleted_idents` attributes by assigning them empty dictionaries. Additionally, it calls the `clear_cache` function to reset the internal cache sets. This operation effectively clears any previously stored information in these sets, ensuring that the object's state is updated correctly.

The relationship between this function and its callers is crucial in maintaining data integrity and preventing potential issues caused by stale cache information. By resetting the cache, the object can accurately track changes made to the database and provide a reliable representation of the system's state.

**Note**: It is essential to call `clear` at strategic points in the code to maintain the accuracy of the internal state and prevent any inconsistencies that may arise from outdated cache information.
***
### FunctionDef clear_cache(self)
**clear_cache**: The function of clear_cache is to reset the internal cache sets.

**Parameters**: None

**Code Description**: This function resets the `_created`, `_updated`, and `_deleted` sets by assigning them empty sets. This operation clears any previously stored information in these sets, effectively resetting the cache for future use.

In the context of the project, `clear_cache` is called by several objects to ensure that the internal state is updated correctly. For instance, when entering or exiting a transactional scope, `clear_cache` is invoked to reset the cache and maintain consistency with the current database state.

The relationship between `clear_cache` and its callers is crucial in ensuring data integrity and preventing potential issues caused by stale cache information. By resetting the cache, these objects can accurately track changes made to the database and provide a reliable representation of the system's state.

**Note**: It is essential to call `clear_cache` at strategic points in the code to maintain the accuracy of the internal state and prevent any inconsistencies that may arise from outdated cache information.
***
### FunctionDef __enter__(self)
**__enter__**: The function of __enter__ is responsible for setting up event listeners to track changes made to the database.

**Parameters**: None

**Code Description**: When entering a transactional scope, this function sets up three event listeners: `after_flush`, `after_commit`, and `after_rollback`. These events are triggered by the database at specific points in its lifecycle. The listeners are set to call corresponding methods on the DBHistory object, which update internal state variables to track changes made to the database.

The `clear_cache` method is also called to reset the internal cache sets, ensuring that any previously stored information is cleared and the cache is updated correctly. This ensures data integrity and prevents potential issues caused by stale cache information.

In the context of the project, this function plays a crucial role in maintaining accurate tracking of changes made to the database. The event listeners and corresponding methods work together to provide a reliable representation of the system's state.

**Note**: It is essential to call `__enter__` at strategic points in the code to maintain the accuracy of the internal state and prevent any inconsistencies that may arise from outdated cache information.

The relationship between `__enter__` and its callees is crucial in ensuring data integrity and preventing potential issues caused by stale cache information. The event listeners and corresponding methods work together to provide a reliable representation of the system's state, making it essential to call `__enter__` at strategic points in the code.
***
### FunctionDef __exit__(self, type, value, traceback)
**__exit__**: The function of __exit__ is responsible for removing event listeners and clearing the cache after exiting a transactional scope.

**Parameters**: None

**Code Description**: When the __exit__ method is called, it removes three event listeners: 'after_flush', 'after_commit', and 'after_soft_rollback'. These event listeners are removed from their respective targets using the `remove_event` function. Additionally, the `clear_cache` method is called to reset the internal cache sets.

The removal of event listeners ensures that any pending events or callbacks are not executed after the transaction has been exited. This helps maintain data integrity and prevents potential issues caused by stale cache information.

The clearing of the cache ensures that any previously stored information in the cache is removed, allowing for accurate tracking of changes made to the database instances. This is particularly important when entering or exiting a transactional scope, as it maintains consistency with the current database state.

**Note**: The removal of event listeners and clearing of the cache are crucial steps in maintaining data integrity and preventing potential issues caused by stale cache information. It is essential to call the __exit__ method at strategic points in the code to ensure accurate tracking of changes made to the database instances.
***
### FunctionDef _populate_idents_dict(self, idents, objects)
**_populate_idents_dict**: The function _populate_idents_dict populates a dictionary with unique identifiers from a list of objects.

**Parameters**:

* **idents**: A dictionary to be populated with unique identifiers.
* **objects**: A list of objects from which the unique identifiers are extracted.

**Code Description**:
The _populate_idents_dict function iterates through the provided list of objects. For each object, it generates a unique identifier using the `util.identity_key` function and adds the corresponding value to the 'idents' dictionary. If the key does not exist in the dictionary, it creates a new set and adds the value to it.

In the context of the project, this function is called by the `_after_commit` method of the DBHistory class. The `_after_commit` method is responsible for updating various dictionaries (created_idents, updated_idents, deleted_idents) with unique identifiers from the objects that were created, updated, or deleted during a database transaction.

The _populate_idents_dict function plays a crucial role in maintaining these dictionaries by extracting and aggregating the unique identifiers from the objects. This information is likely used for tracking changes to the database and ensuring data consistency across different transactions.

**Note**: The function assumes that the 'idents' dictionary is initialized before calling this method, as it relies on its existence to store the extracted unique identifiers.
***
### FunctionDef _after_flush(self, db, flush_context, instances)
**_after_flush**: The function of _after_flush is to update the internal state of the DBHistory object by aggregating the newly created, updated, and deleted instances from the database.

**Parameters**:

* `db`: The database instance that triggered the flush event.
* `flush_context`: The context in which the flush operation was performed.
* `instances`: An optional parameter to specify a set of instances to be processed. Defaults to None.

**Code Description**: This function is called by the DBHistory object when an after_flush event is triggered, indicating that the database has been flushed. It updates three internal sets: `_created`, `_updated`, and `_deleted`. These sets are used to track the changes made to the database instances.

The function first defines a helper function `identityset_to_set` that converts an identity set (a set of objects) into a regular set. This is necessary because the `db.new`, `db.dirty`, and `db.deleted` attributes return identity sets, which cannot be directly added to the internal sets.

The function then updates the `_created` set by adding the newly created instances from the database. It does this by converting the `db.new` identity set into a regular set using the `identityset_to_set` helper function and then unioning it with the existing `_created` set.

Similarly, the function updates the `_updated` set by adding the updated instances from the database, using the `db.dirty` attribute. Finally, it updates the `_deleted` set by adding the deleted instances from the database, using the `db.deleted` attribute.

**Note**: The order in which the sets are updated is important, as it ensures that the internal state of the DBHistory object accurately reflects the changes made to the database.

**Output Example**: The function does not return any value. Instead, it updates the internal state of the DBHistory object by modifying its `_created`, `_updated`, and `_deleted` sets.

In the context of the project, this function is called when an after_flush event is triggered, which typically occurs when a database flush operation is performed. The DBHistory object uses this information to track changes made to the database instances and provide a record of the changes.
#### FunctionDef identityset_to_set(obj)
**identityset_to_set**: The function of identityset_to_set is to convert an object's member values into a set.

**Parameters**:

* **obj**: The input object containing member values to be converted into a set.

**Code Description**:
The `identityset_to_set` function takes an object `obj` as its parameter and returns a set comprising the values of `obj._members`. This function is designed to extract the unique elements from the `_members` attribute of the input object, which are then collected in a set data structure.

In essence, this function serves as a utility for converting the member values into a collection that eliminates duplicates, allowing developers to work with a distinct and unordered set of values.

**Note**: When using `identityset_to_set`, it is essential to ensure that the input object has an `_members` attribute containing the desired values. Failure to do so may result in unexpected behavior or errors.

**Output Example**:
Suppose we have an object `my_obj` with a `_members` attribute containing the following values: `[1, 2, 3, 4, 5]`. When calling `identityset_to_set(my_obj)`, the output would be a set `{1, 2, 3, 4, 5}`, which is a collection of unique elements from the original list.
***
***
### FunctionDef _after_commit(self, db)
**_after_commit**: The function of _after_commit is to update internal state after a database commit operation.

**Parameters**:

* **db**: The database instance that triggered the commit operation.

**Code Description**:
The _after_commit method is called when a database transaction is committed. This method updates three internal dictionaries, `created_idents`, `updated_idents`, and `deleted_idents`, by populating them with unique identifiers from the objects created, updated, or deleted during the transaction. The `_populate_idents_dict` function is used to populate these dictionaries.

The method also calls the `clear_cache` method to reset the internal cache sets, ensuring that any previously stored information is cleared and the cache is updated correctly.

**Note**: This method is called within the _flush method for nested transactions, which is an unexpected behavior. In this case, the method returns immediately without updating the internal state.

The relationship between `_after_commit` and its callers is crucial in maintaining data integrity and preventing potential issues caused by stale cache information. The `clear_cache` method is essential to ensure that the internal state is updated correctly and accurately reflects the current database state.

**Output Example**: This function does not return any output, as it updates internal state rather than producing a result.
***
### FunctionDef _after_rollback(self, db, prev_tx)
**_after_rollback**: The function of _after_rollback is to reset the internal cache sets after a rollback operation.

**Parameters**:

* db: The database object that triggered the rollback.
* prev_tx: The previous transaction that was rolled back.

**Code Description**:
The _after_rollback function is called when a rollback operation occurs, and its purpose is to clear the internal cache sets. This ensures that any previously stored information in these sets is removed, effectively resetting the cache for future use. By doing so, this function maintains data integrity and prevents potential issues caused by stale cache information.

In the context of the project, _after_rollback is called by several objects to ensure that the internal state is updated correctly. For instance, when entering or exiting a transactional scope, _after_rollback is invoked to reset the cache and maintain consistency with the current database state. The relationship between _after_rollback and its callers is crucial in ensuring data integrity and preventing potential issues caused by outdated cache information.

**Note**: It is essential to call _after_rollback at strategic points in the code to maintain the accuracy of the internal state and prevent any inconsistencies that may arise from outdated cache information.
***
