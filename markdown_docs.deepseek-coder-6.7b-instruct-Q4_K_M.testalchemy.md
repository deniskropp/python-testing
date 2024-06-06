## ClassDef sample_property
**sample_property**: The function of sample_property is to act as a descriptor that allows access to an instance method and provides additional functionalities such as automatic database session handling, property tracking, etc. 

**Attributes**:
- `method`: This attribute refers to the original instance method that will be decorated by this descriptor. It should be passed when creating a sample_property object.
- `name`: The name of the property. If not provided, it defaults to the name of the method.

**Code Description**: 
The class `sample_property` is a descriptor that decorates instance methods and provides additional functionalities. When accessed as an attribute on an instance (e.g., object.method), it calls the original method and handles its return value according to certain rules, such as adding returned objects to the database session if they are collections or single instances respectively. It also keeps track of used properties in the `used_properties` set of the instance.

The class is called by various other parts of the project. For example, it's used to decorate methods that return categories when creating sample instances (e.g., `Sample.category()`). 

In some cases, a method may be overridden in subclasses and its original behavior might need to be accessed. This can be done by calling the decorated method directly on an instance of the class: `instance._method()`.

**Note**: The use of this descriptor is optional. It's not used for all methods, but only those that require additional functionality like automatic database session handling and property tracking. 

**Output Example**: Consider a sample instance with two properties, 'method1' and '_method2'. When accessed as attributes, they would be decorated by `sample_property` objects. The original methods could return instances of classes or collections of instances that need to be added to the database session when accessed. 

```python
class Sample:
    method1 = sample_property(some_instance_method)
    _method2 = sample_property(another_instance_method)
```
### FunctionDef __init__(self, method, name)
**__init__**: The function of __init__ is to initialize an instance of the class with a given method and optional name. 

**Parameters**:
- `method`: This parameter represents the method that will be used for initialization. It should be callable (i.e., it can be invoked like a function).
- `name`: This is an optional parameter representing the name of the instance. If not provided, it defaults to the name of the method being used for initialization.

**Code Description**: The code defines an initializer method for the class. It takes two parameters - 'method' and 'name'. 
- When called on a new object, this method sets its own `__doc__` attribute (documentation string) to be the same as the given 'method's documentation string. This allows the instance to inherit the docstring of the provided method.
- The name of the instance is set either by the value passed in or if no value was provided, it defaults to the name of the method being used for initialization. 

**Note**: This initializer provides a way to create instances with custom methods and names without having to manually assign these attributes each time an object is created. It's useful when you have many objects that need similar setup but different behaviors.

***
### FunctionDef __get__(self, inst, cls)
**__get__**: This function is used as a descriptor method that gets called when an attribute of a class is accessed. 

**Parameters**: 
- self: It refers to the instance of the class where this method is being invoked.
- inst: This parameter represents the instance of the class on which the attribute has been accessed. If it's None, then we are accessing the class itself and not an instance of the class.
- cls: This is the class that owns the attribute. 

**Code Description**: The function first checks if 'inst' is None. If True, it means we are accessing the class directly (not creating an instance), so it returns self which refers to the descriptor object itself. Otherwise, it calls the method associated with this descriptor on the instance and stores the result in a variable called 'result'. 

If the result is either a list or tuple, it adds all elements of the result to the database using the add_all() function. If not, it adds the single element to the database using the add() function. It then adds this descriptor's name (self.name) to 'used_properties', sets an attribute with this name on the instance equal to 'result', and finally returns 'result'.

**Note**: This method is used in a specific context where we want to automatically manage database operations when certain attributes of instances are accessed. 

**Output Example**: The function will return the result of calling self.method(inst). If this result is a list or tuple, add_all() will be called; otherwise, add() will be called. No specific output example can be provided as it depends on the context in which __get__ is used.


***
### FunctionDef __call__(self, obj)
**__call__**: The function of __call__ is to execute the method on an input object. 

**Parameters**:
- `obj`: This parameter represents the object on which the method will be executed. It can be any type, as long as it supports the method that this class has defined (i.e., self.method).

**Code Description**: The __call__ function is overridden to allow instances of this class to behave like functions. When called with an object `obj`, it executes the method on `obj` using the instance's own `self.method` attribute. This allows for a more intuitive way to use the class, as if you were calling a function directly on an object.

**Note**: The __call__ magic method is used in Python to make instances of this class callable like functions. It can be called with one argument (the object `obj`). 

**Output Example**: If the instance's `self.method` attribute was a function that multiplied its input by two, and you called it on an integer `5` using the instance of this class, the output would be `10`. This is because the __call__ method executes the method (in this case, multiplication) on the object `obj`.


***
## ClassDef Sample
Sure, here is the detailed explanation of the `Sample` class:

**Sample Class**: The Sample class serves as a base class for other classes in our project. It provides a mechanism to automatically decorate all non-private methods and attributes with certain properties. This can be used to simplify the process of creating objects, handling transactions (with automatic commit or rollback), and managing object relationships.

**Attributes**: 
- `db`: The database session associated with this Sample instance. It's initialized in the constructor and is expected to be an instance of ScopedSession.
- `used_properties`: A set that keeps track of all properties used by this Sample instance. This can help prevent infinite recursion when trying to access related objects.

**Constructor (__init__)**: The constructor initializes the database session and updates the object's attributes with any keyword arguments provided. It also sets `used_properties` to an empty set.

```python
def __init__(self, db, **kwargs):
    if isinstance(db, ScopedSession):
        db = db.registry()
    self.db = db
    self.used_properties = set()
    self.__dict__.update(kwargs)
```

**create_all Method**: This method iterates over all attributes of the Sample instance and creates them in the database if they are not already present. It uses a transaction to ensure that all changes are either committed or rolled back together. 

```python
def create_all(self):
    if self.db.autocommit:
        self.db.begin()
    map(lambda name: getattr(self, name), dir(self))
    self.db.commit()
```

**Note**: The `create_all` method will not create attributes that start with an underscore or are named 'create_all'. It also won't create classmethods, staticmethods, or other special types of methods. This is to prevent infinite recursion when trying to access related objects. 

The Sample class is used throughout our project as a base for many other classes. Its use allows us to handle transactions and manage object relationships in a consistent way across the entire codebase. It's also useful because it automatically decorates all non-private methods with certain properties, which can simplify the process of creating objects and managing their relationships.

### ClassDef __metaclass__
**__metaclass__: The function of __metaclass__ is to define the metaclass of a class. A metaclass is essentially a factory that creates classes, just like a class is a factory for objects. In Python, by default, every class you create has an associated metaclass which is type. However, it's possible to override this default behavior by defining a __metaclass__ attribute in your class definition.

**attributes:**
- cls_name: The name of the class being created.
- bases: A tuple containing the base classes that the new class should be derived from.
- attributes: A dictionary containing the namespace (attribute and method) of the new class.

**Code Description:** This metaclass is used to decorate a class, which will automatically convert all non-underscore methods into properties with getter and setter methods. It also skips certain methods like 'create_all'. If an attribute is already decorated from another class, it uses the original method as the new value.

**Note:** This metaclass is used to simplify the process of defining classes in a way that's more intuitive for developers and reduces boilerplate code. It also provides automatic property decorations which can be useful for creating data models or API representations.

**Output Example:** A class decorated with __metaclass__ would look like this:
```python
class MyClass(object):
    __metaclass__ = SampleMetaclass
    
    def my_method(self):
        pass
```
In the above example, 'my_method' will be automatically converted into a property with getter and setter methods.

#### FunctionDef __new__(cls, cls_name, bases, attributes)
Sure, here is your requested document:

**__new__**: The function of __new__ is to create and initialize an instance of a class. It's called automatically when you use the `type` built-in function or subclass it with `metaclass=MyMetaClass`. 

**Parameters**:
- cls: This parameter refers to the current class being created.
- cls_name: The name of the class being created.
- bases: A tuple containing the base classes for the new class.
- attributes: A dictionary containing the namespace (attributes and methods) for the new class.

**Code Description**: 
The __new__ method is a special method that's called when an object is created from a class, but before the initialization of the object takes place. It receives the same arguments as the regular constructor, plus one additional argument (cls), which refers to the class itself. The purpose of this method is to create and initialize the instance of the new class.

In our code, we are overriding __new__ to customize its behavior. We first call `type.__new__(cls, cls_name, bases, attributes)` to create a new object of type cls. Then, for each attribute in the newly created object, if it's an instance method (an instance of types.MethodType), we store its underlying function in `new_value`. If it's an instance of `sample_property` and has a different name than the current attribute, we also store its original method in `new_value`.

Finally, for each attribute that was processed (i.e., not starting with '_', 'create_all', or is an instance of types.MethodType or sample_property), we create a new `sample_property` object and set it as the value of the corresponding attribute in the newly created object. This allows us to access these methods as properties, providing additional functionality such as automatic database session handling and property tracking.

**Note**: The __new__ method is called automatically when creating an instance of a class, so we usually don't need to call it manually. However, in our case, we are using `type.__new__(cls, cls_name, bases, attributes)` to create the new object because we want to customize its behavior before the initialization takes place.

**Output Example**: Consider a class 'MyClass' with two instance methods, 'method1' and '_method2'. When an instance of 'MyClass' is created, __new__ will be called automatically, and it will decorate these methods as `sample_property` objects. The original methods could return instances of classes or collections of instances that need to be added to the database session when accessed. 

```python
class MyClass:
    method1 = sample_property(some_instance_method)
    _method2 = sample_property(another_instance_method)
```
Raw code:```
class MyClass:
    def __new__(cls, cls_name, bases, attributes):
        self = type.__new__(cls, cls_name, bases, attributes)
        for name in dir(self):
            if name.startswith('_') or name == 'create_all':
                continue
            value = getattr(self, name)
            if isinstance(value, types.MethodType):
                new_value = value.im_func
            elif isinstance(value, sample_property) and name != value.name:
                new_value = value.method
            else:
                continue
            setattr(self, name, sample_property(new_value, name=name))
        return self
```

***
***
### FunctionDef __init__(self, db)
Sure, here is your requested documentation:

**__init__**: The function of __init__ is to initialize an instance of the Sample class with a database session and any additional keyword arguments. 

**Parameters**:
- db: This parameter represents the database session which could be either a ScopedSession or another type. If it's a ScopedSession, it will be converted into its registry form.
- **kwargs: Any number of key-value pairs that can be used to set attributes on the instance. These are passed directly to the __dict__ update method.

**Code Description**: 
The function starts by checking if the provided db is an instance of ScopedSession. If it is, then it converts the db into its registry form. It then assigns this converted or unconverted db to self.db and initializes a set called used_properties. Finally, it updates the __dict__ of the instance with any keyword arguments provided.

**Note**: This function allows for flexibility in how instances are initialized by allowing users to pass additional attributes when creating an instance. It's important to note that this could potentially lead to confusion if not handled carefully as it can overwrite existing attributes on the instance.


***
### FunctionDef create_all(self)
Sure, here is the detailed explanation of the `create_all` function:

**Function Name**: create_all

**Parameters**: 
- self: This refers to the instance of the class where this method is called. It's a convention in Python that allows methods to access attributes and other methods of the object they are part of.

**Code Description**: The `create_all` function is designed to create all necessary tables or collections in the database associated with the current session. This is achieved by iterating over all the methods of the class instance, checking if each method returns an instance of a model (which presumably represents a table), and if so, adding it to the session for creation.

The function starts by initiating a transaction if `self.db.autocommit` is True. Then it uses Python's built-in `map` function along with `getattr` to iterate over all methods of the instance (excluding special methods like `__init__` and `create_all`). For each method, it checks if the return value is an instance of a model class. If so, it adds this instance to the session for creation.

After adding all instances to be created, the function commits the transaction. This means that all tables or collections will be created in the database as soon as possible. 

**Note**: The `create_all` method should only be called once per application run, typically at startup when the application is first set up and before any other operations are performed on the database. It's not recommended to call it multiple times within a single application run because this can lead to unexpected behavior or errors.

***
## ClassDef Restorable
**Restorable**: This class is designed to manage database transactions by providing an interface that allows developers to easily rollback changes made during a transaction if any exception occurs. 

**Attributes**:
- `db`: The SQLAlchemy session or registry object used for the transaction. If it's a ScopedSession instance, we convert it into its underlying registry.
- `watch`: The entity to watch for changes during the transaction. Default is set to the database itself.
- `history`: A dictionary that stores identities of entities created or modified in the current transaction. 

**Code Description**: This class provides a context manager interface (using Python's built-in `__enter__` and `__exit__` methods) for managing transactions. When entering the context, it registers an 'after_flush' event listener to watch changes made during the transaction. On exiting the context, it rolls back all changes, expunges all tracked objects from the session, commits the current transaction, closes the database connection and removes the 'after_flush' event listener. If any exception occurs within the context, the `__exit__` method will be invoked to handle the exception by rolling back the transaction and removing the registered event listener.

**Note**: This class is useful when you want to ensure data integrity in your database transactions. It can help prevent data loss if an error occurs during a transaction. However, it's important to note that this class does not provide any mechanism for recovering from errors or handling exceptions other than rolling back the transaction and removing event listeners.

### FunctionDef __init__(self, db, watch)
**__init__:** The function of __init__ is to initialize an instance of the Restorable class with a database session and optional watch parameter. 

**Parameters:**
- db: This parameter represents the database session that will be used by the Restorable object. It can either be an instance of ScopedSession or any other type, in which case it is converted to its corresponding registry.
- watch (optional): If not provided, this defaults to the value of 'db'. Otherwise, it takes the value passed as the argument. 

**Code Description:** The function sets up a new instance of Restorable with the given database session and optional watch parameter. It also initializes an empty dictionary called 'history' which will be used to store changes made to the database.

**Note:** This constructor is typically invoked when creating a new instance of the Restorable class, providing it with a database session and optionally specifying what parts of the database should be watched for changes. The watch parameter can be used to optimize performance by only monitoring specific areas of the database.

***
### FunctionDef __enter__(self)
**__enter__**: The function of __enter__ is to set up an event listener that will be triggered after a flush event occurs in SQLAlchemy database. 

**Parameters**:
- `self`: This refers to the instance of the class that contains this method, which is an instance of Restorable.
- `db`: This parameter represents the current session in SQLAlchemy. It's used to interact with the database.
- `flush_context`: The context for the flush event. Not clear what it refers to without additional information.
- `instances`: A list of instances that were flushed during the transaction. If not provided, all new instances in the session will be processed.

**Code Description**: 
The function starts by listening to a 'after_flush' event on the database using SQLAlchemy's event system. When this event occurs, it triggers the `self.after_flush` method with the current session (db), the flush context and optionally a list of instances that were flushed during the transaction.

The purpose of this function is to manage database transactions in an object-relational mapping (ORM) system like SQLAlchemy, which automatically manages database transactions and provides additional functionality such as automatic data validation and querying. It's likely part of a larger codebase that uses SQLAlchemy for managing its database operations.

**Note**: 
The `after_flush` event listener is typically set up in a context manager that uses this function to handle the after flush event. The exact usage of this function would depend on how it's used within the larger codebase, which isn't provided here.

Raw code:```
    def __enter__(self):
        event.listen(self.watch, 'after_flush', self.after_flush)
```==========
***
### FunctionDef __exit__(self, type, value, traceback)
**__exit__**: The function of __exit__ is to handle database operations when an exit event occurs. 

**Parameters**:
- `self`: This refers to the instance of the class that contains this method, which is an instance of Restorable.
- `type`: It represents the type of exception if any occurred during the execution of the code within the context manager.
- `value`: It holds the value of the exception if any occurred during the execution of the code within the context manager.
- `traceback`: It provides information about where and why an error occurred, which is useful for debugging purposes.

**Code Description**: 
The function starts by rolling back all changes made in the current transaction with the database (db.rollback()). This ensures that if any errors occur during the execution of subsequent code within the context manager, these changes will not be committed to the database. The function then removes all instances from the session and sets autoflush to False. If autocommit is enabled for the current transaction, it starts a new transaction (db.begin()). Finally, it iterates over each instance in the history set of the Restorable instance and deletes them from the database. After deleting all instances, it commits the changes to the database (db.commit()) and closes the connection to the database (db.close()). It then sets autoflush back to its original value and removes the 'after_flush' event listener.

**Note**: 
The __exit__ function is part of a context manager that uses this function to handle the exit event. The exact usage of this function would depend on how it's used within the larger codebase, which isn't provided here. It's designed to manage database transactions and provide additional functionality such as automatic data validation and querying.

Raw code:```
    def __exit__(self, type, value, traceback):
        db = self.db
        db.rollback()
        db.expunge_all()
        old_autoflush = db.autoflush
        db.autoflush = False
        if db.autocommit:
            db.begin()
        for cls, ident_set in self.history.items():
            for ident in ident_set:
                instance = db.query(cls).get(ident)
                if instance is not None:
                    db.delete(instance)
        db.commit()
        db.close()
        db.autoflush = old_autoflush
        remove_event(self.watch, 'after_flush', self.after_flush)
```

***
### FunctionDef after_flush(self, db, flush_context, instances)
**after_flush**: The function of after_flush is to handle database operations after a flush event occurs. 

**Parameters**:
- `self`: This refers to the instance of the class that contains this method, which is an instance of Restorable.
- `db`: This parameter represents the current session in SQLAlchemy. It's used to interact with the database.
- `flush_context`: The context for the flush event. Not clear what it refers to without additional information.
- `instances`: A list of instances that were flushed during the transaction. If not provided, all new instances in the session will be processed.

**Code Description**: 
The function starts by iterating over each instance in the 'new' attribute of the database session (db). For each instance, it retrieves its class and identity key using a utility function from SQLAlchemy. The retrieved class and identity are then added to a set associated with that class in the `history` attribute of the Restorable instance.

The purpose of this function seems to be to keep track of instances that have been newly created during a transaction, so they can later be deleted if necessary (e.g., when rolling back the transaction). This is likely part of an object-relational mapping (ORM) system like SQLAlchemy, which automatically manages database transactions and provides additional functionality such as automatic data validation and querying.

**Note**: 
The `after_flush` event listener is typically set up in a context manager that uses this function to handle the after flush event. The exact usage of this function would depend on how it's used within the larger codebase, which isn't provided here.

***
## ClassDef DBHistory
An unknown error occurred while generating this documentation after many tries.
### FunctionDef __init__(self, session)
Sure, here is the detailed explanation of the `__init__` function:

**__init__**: The function of __init__ is to initialize an instance of DBHistory class with a session object. 

**Parameters**: 
- `session`: This parameter should be either an instance of Session or ScopedSession class. It's used as the database session for this instance of DBHistory.

**Code Description**: The function starts by asserting that the provided session is either a Session or a ScopedSession object. If it is, then `session` is assigned to self.session. 

The function also initializes three empty sets (self._created, self._deleted, and self._updated) which will be used to keep track of created, updated, and deleted objects in the session respectively. It also initializes three dictionaries (self.created_idents, self.updated_idents, and self.deleted_idents) that will store identities of these objects.

The function then checks if the provided session is a ScopedSession object. If it is, it assigns the registry of this session to `self._target` instead of `session`. This is done because in SQLAlchemy's scoped sessions, each thread has its own session that is independent from other threads'.

**Note**: The use of ScopedSession can be beneficial when dealing with multiple threads as it ensures that each thread gets its own session which doesn't interfere with the others. However, this also means that changes made in one thread are not visible to other threads until they commit their transactions. 

This function is typically called at the start of a new request and creates an instance of DBHistory for tracking database operations within that request.

***
### FunctionDef last(self, model_cls, mode)
**last**: The function of last is to return a set of identifiers based on the given mode ('created', 'updated', or 'deleted') and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.
- mode: This parameter can be one of three strings, 'created', 'updated', or 'deleted'. It determines which set of identifiers to return.

**Code Description**: 
The `last` method is a helper function that retrieves a set of identifiers for instances of a given model class based on the specified mode ('created', 'updated', or 'deleted'). The identifiers are stored in instance variables (named as '{mode}_idents') and accessed via getattr(). If no identifiers exist for the given model class and mode, an empty set is returned.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode}_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than 'created', 'updated', or 'deleted' as an argument, it will raise an AssertionError.

**Output Example**: 
If the model class is `MyModel` and the mode is 'created', the function might return a set like this: {1, 2, 3}. This means that there are three instances of MyModel created with identifiers 1, 2, and 3.

***
### FunctionDef _idents_to_objects_set(self, idents, model_cls)
**_idents_to_objects_set**: The function of _idents_to_objects_set is to convert identifiers into objects using SQLAlchemy's query method. 

**Parameters**:
- idents: A list of identifiers that will be converted into objects.
- model_cls: The class of the database model used in the conversion.

**Code Description**: This function utilizes SQLAlchemy's query method to convert a list of identifiers (idents) into a set of objects from the specified model class (model_cls). It does this by creating a new instance of the provided model class for each identifier and storing these instances in a Python set.

**Note**: The function relies on SQLAlchemy's query method to retrieve objects, which is an essential part of interacting with databases using SQLAlchemy. If the identifiers do not correspond to any existing objects in the database, None will be returned for those identifiers.

**Output Example**: Given a list of identifiers [1, 2, 3] and a model class Model, _idents_to_objects_set would return a set containing three instances of Model with ids 1, 2, and 3.

The function is called by the following objects in the project:
- last_created: This object uses _idents_to_objects_set to convert identifiers into objects for the 'last created' records from a specified model class.
- last_updated: Similar to last_created, this object also uses _idents_to_objects_set to convert identifiers into objects for the 'last updated' records from a specified model class.
- assert_created: This object uses _idents_to_objects_set to ensure that all provided identifiers correspond to existing 'created' records in a specified model class.
- assert_updated: Similar to assert_created, this object also uses _idents_to_objects_set to ensure that all provided identifiers correspond to existing 'updated' records in a specified model class.

***
### FunctionDef last_created(self, model_cls)
Sure, here is the detailed explanation document for this function:

**last_created**: The function of last_created is to return a set of identifiers based on the given mode  ('created', 'updated', or 'deleted') and model class.

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.

**Code Description**: 
The `last` method is a helper function that retrieves a set of identifiers for instances of a given model class based on the specified mode ('created', ‘updated’, or 'deleted'). The identifiers are stored in instance variables (named as '{mode}_idents') and accessed via getattr(). If no identifiers exist for the given model class and mode, an empty set is returned.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode}_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than 'created', 'updated', or 'deleted' as an argument, it will raise an AssertionError.

**Output Example**: 
If the model class is `MyModel` and the mode is 'created', the function might return a set like this: {1, 2, 3}. This means that there are three instances of MyModel created with identifiers 1, 2, and 3.

The function is called by the following objects in the project:
- last_created: This object uses `last_created` to return a set of identifiers for the 'last created' records from a specified model class.
- assert_created: This object uses `last_created` to ensure that all provided identifiers correspond to existing 'created' records in a specified model class.

The function is also called by these objects, their code and docs are as following:
- tests.py/Test/test_models_history_init: The test case initializes the DBHistory object and checks if the created, updated, and deleted identifiers are empty at initialization.
- tests.py/Test/test_models_history_created: The test case creates a User instance and adds it to the session. After committing the changes, `last_created` is called with the User class as an argument to check if the created identifiers of the User are correct.
- tests.py/Test/test_models_history_updated: The test case updates a User instance's name and checks if the updated identifiers of the User are correct after committing the changes.
- tests.py/Test/test_models_history_de
***
### FunctionDef last_updated(self, model_cls)
Sure, here is the detailed explanation document for this object based on the code of the target object itself and its calling situation in the project:

**last_updated**: The function `last_updated` is used to return a set of objects that represent instances of a given model class based on the specified mode ('created', 'updated', or 'deleted'). 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.

**Code Description**: 
The `last_updated` method utilizes two other helper functions to retrieve a set of objects from a given model class based on the specified mode ('created', 'updated', or 'deleted'). The function first calls `self._idents_to_objects_set` with the identifiers returned by `self.last(model_cls, 'updated')` and the model class as arguments to convert these identifiers into objects.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode}_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than 'created', 'updated', or 'deleted' as an argument, it will raise an AssertionError.

**Output Example**: 
If the model class is `MyModel` and the mode is 'updated', the function might return a set containing three instances of MyModel with ids 1, 2, and 3. This means that there are three instances of MyModel updated in the database.

The function is called by the following objects in the project:
- last_updated: This object uses `last_updated` to get the 'last updated' records from a specified model class.

Raw code:```
    def last_updated(self, model_cls):
        return self._idents_to_objects_set(
            self.last(model_cls, 'updated'),
            model_cls
         )

```==========

***
### FunctionDef last_deleted(self, model_cls)
Sure, here is your requested detailed explanation document:

**last_deleted**: The function of `last_deleted` is to return identifiers based on the given model class and mode ('created', 'updated', or 'deleted'). 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.

**Code Description**: 
The `last_deleted` method is a helper function that retrieves identifiers for instances of a given model class based on the specified mode ('created', 'updated', or 'deleted'). The identifiers are stored in instance variables (named as '{mode}_idents') and accessed via getattr(). If no identifiers exist for the given model class and mode, an empty set is returned.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode}_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than 'created', 'updated', or 'deleted' as an argument, it will raise an AssertionError.

**Output Example**: 
If the model class is `MyModel` and the mode is 'created', the function might return a set like this: {1, 2, 3}. This means that there are three instances of MyModel created with identifiers 1, 2, and 3.

This function is called by various test cases in the project to verify the correctness of the history tracking mechanism implemented in `DBHistory` class. For example, it's used to check if new instances of a model are correctly tracked as 'created', or if existing instances are correctly tracked as 'updated'.

***
### FunctionDef assert_(self, model_cls, ident, mode)
**assert_**: The function of assert_ is to validate if instances exist based on given identifiers and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.
- ident: This parameter can be either a single identifier or a tuple/list of identifiers. If it's provided, the function will validate if these identifiers exist in the set returned by `last` method.
- mode: This parameter can be one of three strings, ‘created’, ‘updated’, or ‘deleted’. It determines which set of identifiers to return and validate against.

**Code Description**: The function first retrieves a set of identifiers for instances of a given model class based on the specified mode ('created', 'updated', or 'deleted') using `last` method. If no identifiers exist, an AssertionError is raised with a specific error message. Then it checks if the provided identifier(s) are in this set. If not, another AssertionError is raised.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode}_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than ‘created’, ‘updated’, or ‘deleted’ as an argument, it will raise an AssertionError.

**Output Example**: If the model class is `MyModel` and the identifiers are [1,2,3], the function might return a set like this: {1, 2, 3}. This means that there are three instances of MyModel with identifiers 1, 2, and 3.

**Reference Relationship**: The `assert_` method is called by other methods such as `assert_created`, `assert_updated`, and `assert_deleted` to validate if specific instances exist based on given identifiers and model class. These methods are used in the context of testing database operations like creation, update, or deletion of data models.

***
### FunctionDef assert_created(self, model_cls, ident)
Sure, here is the detailed explanation document for this function:

**assert_created**: The function of assert_created is to validate if instances exist based on given identifiers and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.
- ident: This parameter can be either a single identifier or a tuple/list of identifiers. If it's provided, the function will validate if these identifiers exist in the set returned by `last` method.
- mode: This parameter can be one of three strings, ‘created’, ‘updated’, or ‘deleted’. It determines which set of identifiers to return and validate against.

**Code Description**: The function first retrieves a set of identifiers for instances of a given model class based on the specified mode ('created', 'updated', or 'deleted') using `last` method. If no identifiers exist, an AssertionError is raised with a specific error message. Then it checks if the provided identifier(s) are in this set. If not, another AssertionError is raised.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode}_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than ‘created’, ‘updated’, or ‘deleted’ as an argument, it will raise an AssertionError.

**Output Example**: If the model class is `MyModel` and the identifiers are [1,2,3], the function might return a set like this: {1, 2, 3}. This means that there are three instances of MyModel with identifiers 1, 2, and 3.

**Reference Relationship**: The `assert_` method is called by other methods such as `assert_created`, `assert_updated`, and `assert_deleted` to validate if specific instances exist based on given identifiers and model class. These methods are used in the context of testing database operations like creation, update, or deletion of data models.

Raw code:```
    def assert_created(self, model_cls, ident=None):
        return self._idents_to_objects_set(
            self.assert_(model_cls, ident, ‘created’),
            model_cls
         )

```==========

***
### FunctionDef assert_updated(self, model_cls, ident)
Sure, here is the detailed explanation document for this function:

**assert_updated**: The function of assert_updated is to validate if instances exist based on given identifiers and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.
- ident: This parameter can be either a single identifier or a tuple/list of identifiers. If it's provided, the function will validate if these identifiers exist in the set returned by `last` method.
- mode: This parameter can be one of three strings, ‘created’, ‘updated’, or ‘deleted’. It determines which set of identifiers to return and validate against.

**Code Description**: The function first retrieves a set of identifiers for instances of a given model class based on the specified mode ‘created’, ‘updated’, or ‘deleted’ using `last` method. If no identifiers exist, an AssertionError is raised with a specific error message. Then it checks if the provided identifier(s) are in this set. If not, another AssertionError is raised.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The '{mode
***
### FunctionDef assert_deleted(self, model_cls, ident)
Sure, here is the detailed explanation document for this function:

**assert_deleted**: This function validates if instances exist based on given identifiers and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.
- ident: This parameter can be either a single identifier or a tuple/list of identifiers. If it's provided, the function will validate if these identifiers exist in the set returned by `last` method.
- mode: This parameter can be one of three strings, ‘created’, ‘updated’, or ‘deleted’. It determines which set of identifiers to return and validate against.

**Code Description**: The function first retrieves a set of identifiers for instances of a given model class based on the specified mode ‘deleted’ using `last` method. If no identifiers exist, an AssertionError is raised with a specific error message. Then it checks if the provided identifier(s) are in this set. If not, another AssertionError is raised.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The 'deleted_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than ‘created’, ‘updated’, or ‘deleted’ as an argument, it will raise an AssertionError.

**Output Example**: If the model class is `MyModel` and the identifiers are [1,2,3], the function might return a set like this: {1, 2, 3}. This means that there are three instances of MyModel with identifiers 1, 2, and 3.

**Reference Relationship**: The `assert_deleted` method is called by other methods such as `assert_deleted_one` to validate if specific instances exist based on given identifiers and model class. These methods are used in the context of testing database operations like deletion of data models.

***
### FunctionDef assert_one(self, dataset, model_cls, mode)
**assert_one**: The function of assert_one is to ensure that there is only one instance of a specific model class in a dataset. 

**Parameters**:
- `dataset`: This parameter represents the dataset to be checked, which should contain instances of the specified model class.
- `model_cls`: This parameter specifies the type of model class that we are checking for in the dataset.
- `mode`: The mode indicates what action was performed on the data set (created, updated or deleted). 

**Code Description**: This function checks if there is only one instance of a specific model class in the given dataset. If not, it raises an AssertionError with a message indicating how many instances were found and which model class they belong to. The function then returns this single instance from the dataset.

This function is commonly used in testing scenarios where we want to ensure that certain actions have only resulted in one instance of a specific model class being present in our database or data set. For example, it might be used after calling `assert_created` or `assert_deleted` functions to check if exactly one instance of the specified model class has been created or deleted.

**Note**: This function assumes that the dataset is a list-like object and that instances are popped from it in the order they were added. If this assumption does not hold, the behavior of `assert_one` will be undefined.

**Output Example**: Given a dataset containing three instances of model class 'User', calling `assert_one(dataset, User, 'created')` would return the last instance ('User 3'), raising an AssertionError if there were more or less than one instance in the dataset.

***
### FunctionDef assert_created_one(self, model_cls)
Sure, here is the detailed explanation document for this function:

**assert_created_one**: The function of assert_created_one is to validate if exactly one instance of a specific model class exists based on given identifiers. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.

**Code Description**: The function first calls `assert_created` method with provided parameters and checks if exactly one instance exists in the returned set. If not, an AssertionError is raised with a specific error message. Then it returns this single instance from the dataset.

**Note**: 
- This function assumes that identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The 'created_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than ‘created’, ‘updated’, or ‘deleted’ as an argument, it will raise an AssertionError.

**Output Example**: Given a model class `MyModel` and identifiers [1], the function might return instance of MyModel with identifier 1 if exactly one instance exists in the database.

**Reference Relationship**: The `assert_created_one` method is called by other methods such as `test_models_history_created` to validate if exactly one instance of a specific model class has been created after certain operations have taken place. These methods are used in testing scenarios where we want to ensure that database operations like creation of data models result in only one instance being present in the database.

Raw code:```
    def assert_created_one(self, model_cls):
        result = self.assert_created(model_cls)
        return self.assert_one(result, model_cls, 'created')

```==========
Also, the code has been called by the following objects, their code and docs are as following:
obj: tests.py/Test/test_models_history_created
Document: 
None
Raw code:```
    def test_models_history_created(self):
        session = self.session
        with DBHistory(session) as history:
            user = User(name='test')
            session.add(user)
            session.commit()
            self.assertEqual(history.created_idents, {User: set([(1,)])})
            self.assertEqual(history.updated_idents,  {})
            self.assertEqual(history.deleted_idents,  {})
            self.assertEqual(history.last_created(User), set([user]))
            self.assertEqual(history.last_updated(User), set())
            self.assertEqual(history.last_deleted(User), set())
            self.assertEqual(history.assert_created(User), set([user]))
            self.assertEqual(history.assert_created(User, user.id), set([user]))
           
***
### FunctionDef assert_deleted_one(self, model_cls)
Sure, here is the detailed explanation document for this function:

**assert_deleted_one**: This function validates if exactly one instance of a specific model class has been deleted based on given identifiers and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.

**Code Description**: The function first validates if exactly one instance of a specific model class has been deleted based on provided identifiers using `assert_deleted` method. If not, an AssertionError is raised with a specific error message. Then it checks if the provided identifier(s) are in this set. If not, another AssertionError is raised.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. The 'deleted_idents' attribute should be a dictionary like this.
- If you try to pass a mode other than ‘created’, ‘updated’, or ‘deleted’ as an argument, it will raise an AssertionError.

**Output Example**: If the model class is `MyModel` and the identifiers are [1], the function might return a set like this: {(1,)}. This means that there is one instance of MyModel with identifier 1 has been deleted.

**Reference Relationship**: The `assert_deleted_one` method is used in the context of testing database operations like deletion of data models. It's called by other methods such as `test_models_history_deleted` to validate if exactly one instance of a specific model class has been deleted based on given identifiers and model class.

Raw code:```
    def assert_deleted_one(self, model_cls):
        result = self.assert_deleted(model_cls)
        return self.assert_one(result, model_cls, ‘deleted’)

```==========

***
### FunctionDef assert_updated_one(self, model_cls)
Sure, here is the detailed explanation document for this function:

**assert_updated_one**: The function of assert_updated_one is to validate if an instance has been updated based on given identifiers and model class. 

**Parameters**:
- self: This parameter refers to the instance of the object that calls this method. It's automatically passed by Python when you call an instance method, which is why it doesn't need to be explicitly mentioned in the documentation.
- model_cls: This parameter should be a class that represents a data model. The function will return identifiers for instances of this model class based on the given mode.

**Code Description**: The function first retrieves a set of identifiers for instances of a given model class based on the specified mode 'updated' using `assert_updated` method. If no identifiers exist, an AssertionError is raised with a specific error message. Then it checks if the provided identifier(s) are in this set. If not, another AssertionError is raised. The function then returns one instance from the dataset based on the given model class and mode using `assert_one` method.

**Note**: 
- This function assumes that the identifiers are stored in a dictionary where keys are model classes and values are sets of identifiers. If this assumption does not hold, the behavior of `assert_updated_one` will be undefined.

**Output Example**: Given a dataset containing three instances of model class 'User', calling `assert_updated_one(User)` would return one instance from the set ('User 3'), raising an AssertionError if there were more or less than one instance in the dataset.

This function is commonly used in testing scenarios where we want to ensure that certain actions have resulted in exactly one instance of a specific model class being present in our database or data set after updating. For example, it might be used after calling `assert_created` or `assert_deleted` functions to check if exactly one instance of the specified model class has been created or deleted after updating.

The function is called by several test cases in tests.py file for different scenarios like testing history creation, updated and deletion with scoped session. The detailed documentations can be found at `tests.py/Test/test_models_history_created`, `tests.py/Test/test_models_history_updated` and `tests.py/Test/test_models_history_deleted`.

***
### FunctionDef assert_nothing_happened(self)
**assert_nothing_happened**: The function of assert_nothing_happened is to check if there are any changes (creations, updates or deletions) made to the database within its scope. 

**Parameters**: This Function does not take any parameters.

**Code Description**: The `assert_nothing_happened` method checks whether there were any modifications to the database records that occurred during the lifetime of the DBHistory instance (i.e., between the calls to `__enter__()` and `__exit__()`). If any changes were made, it raises an AssertionError with a message indicating what kind of change was made.

**Note**: This function is used in unit tests for database operations to ensure that no unexpected modifications have occurred during the test. It's part of a testing strategy known as "Database Isolation" where each test operates on its own copy of the data, ensuring that tests do not interfere with each other and can be run independently.

**Relationship with Callers**: The `assert_nothing_happened` method is called by unit tests in the project to ensure that no unexpected database changes have occurred during a test. This helps maintain the integrity of the data and ensures that tests are reliable and repeatable. It's used as part of an overall testing strategy known as "Database Isolation".

***
### FunctionDef clear(self)
Sure, here is the detailed explanation document for this function:

**clear**: The function of clear is to reset three sets (`self.created_idents`, `self.updated_idents`, and `self.deleted_idents`) that keep track of changes made in a database session. 

**Parameters**: This function does not take any parameters. It operates on the instance variables of the same class.

**Code Description**: The code initializes three empty sets (`self.created_idents`, `self.updated_idents`, and `self.deleted_idents`) that are used to keep track of changes made in a database session. When a change is detected (for example, an object is created, updated, or deleted), the corresponding identifier of this object is added to one of these sets. The clear function then resets all three sets, effectively clearing any recorded changes from the previous session.

The `clear_cache` function is called by several other functions in the same class (`DBHistory`). Specifically, it's called by the following methods: 
- `__enter__`: The `__enter__` method of a context manager sets up the database history tracking and calls `clear_cache` to clear any previous changes.
- `__exit__`: The `__exit__` method cleans up after exiting the context, calling `clear_cache` again to ensure that no lingering changes are recorded in the session.
- `_after_commit`: This private method is called by SQLAlchemy's event system after a successful commit of a transaction. It populates the `created_idents`, `updated_ids`, and `deleted_idents` dictionaries with identifiers of newly created, updated, or deleted objects in this transaction, and then calls `clear_cache` to clear these identifiers from their respective sets.
- `_after_rollback`: This private method is called by SQLAlchemy's event system after a rollback of a transaction. It simply calls `clear_cache` to clear any lingering changes in the session. 

This function plays an important role in maintaining and tracking database history, ensuring that only relevant changes are recorded and processed.

Raw code:```
    def clear(self):
        self.created_idents = {}
        self.updated_idents = {}
        self.deleted_idents = {}
        self.clear_cache()

```==========

***
### FunctionDef clear_cache(self)
Sure, here is the detailed explanation document for this function:

**clear_cache**: The function of clear_cache is to reset three sets (`self._created`, `self._updated`, and `self._deleted`) that keep track of changes made in a database session. 

**Parameters**: This function does not take any parameters. It operates on the instance variables of the same class.

**Code Description**: The code initializes three empty sets (`self._created`, `self._updated`, and `self._deleted`) that are used to keep track of changes made in a database session. When a change is detected (for example, an object is created, updated, or deleted), the corresponding identifier of this object is added to one of these sets. The `clear_cache` function then resets all three sets, effectively clearing any recorded changes from the previous session.

**Note**: This function is called by several other functions in the same class (`DBHistory`). Specifically, it's called by the following methods: 
- `__enter__`: The `__enter__` method of a context manager sets up the database history tracking and calls `clear_cache` to clear any previous changes.
- `__exit__`: The `__exit__` method cleans up after exiting the context, calling `clear_cache` again to ensure that no lingering changes are recorded in the session.
- `_after_commit`: This private method is called by SQLAlchemy's event system after a successful commit of a transaction. It populates the `created_idents`, `updated_ids`, and `deleted_idents` dictionaries with identifiers of newly created, updated, or deleted objects in this transaction, and then calls `clear_cache` to clear these identifiers from their respective sets.
- `_after_rollback`: This private method is called by SQLAlchemy's event system after a rollback of a transaction. It simply calls `clear_cache` to clear any lingering changes in the session. 

This function plays an important role in maintaining and tracking database history, ensuring that only relevant changes are recorded and processed.

***
### FunctionDef __enter__(self)
Sure, here is the detailed explanation document for this function:

**__enter__**: The function of __enter__ is to set up the database history tracking and clear any previous changes in a database session when entering a context manager block. 

**Parameters**: This function does not take any parameters. It operates on the instance variables of the same class.

**Code Description**: When called, this method sets up three event listeners for the target object (`self._target`). These listeners are triggered after each flush operation ('after_flush'), commit operation ('after_commit'), and rollback operation ('after_soft_rollback'). The `__enter__` method also calls the `clear_cache` function to reset all three sets – `self._created`, `self._updated`, and `self._deleted` – that keep track of changes made in a database session.

**Note**: This function is called by several other functions in the same class (`DBHistory`) after a successful commit operation or a rollback operation. Specifically, it's called by the following methods: 
- `__exit__`: The `__exit__` method cleans up after exiting the context, calling `clear_cache` to ensure that no lingering changes are recorded in the session. This function is also called when a commit operation fails and triggers a rollback. In this case, it's used to clear any lingering changes in the session before retrying the commit operation.
- `_after_commit`: This private method is called by SQLAlchemy's event system after a successful commit of a transaction. It populates the `created_idents`, `updated_ids`, and `deleted_idents` dictionaries with identifiers of newly created, updated, or deleted objects in this transaction, and then calls `clear_cache` to clear these identifiers from their respective sets.
- `_after_rollback`: This private method is called by SQLAlchemy's event system after a rollback of a transaction. It simply calls `clear_cache` to clear any lingering changes in the session. 

This function plays an important role in maintaining and tracking database history, ensuring that only relevant changes are recorded and processed.

**Output Example**: The return value of this function is the instance itself (`self`). This allows for method chaining when using the `__enter__` method inside a context manager block. 

Raw code:```
    def __enter__(self):
        event.listen(self._target, 'after_flush', self._after_flush)
        event.listen(self._target, 'after_commit', self._after_commit)
        event.listen(self._target, 'after_soft_rollback',
                     self._after_rollback)
        self.clear_cache()
        return self

```==========

***
### FunctionDef __exit__(self, type, value, traceback)
Sure, here is the detailed explanation document for this function:

**__exit__**: The function of __exit__ is to clean up after exiting the context manager block by removing event listeners and clearing any cached data. 

**Parameters**: This function takes three parameters:
- `type`: It represents the type of exception that was raised during the execution of the code within the context manager, if any. If no exception occurred, it's None.
- `value`: It holds the value of the exception that was raised, if any. If no exception occurred, it's also None.
- `traceback`: It represents the traceback object associated with the exception, if any. If no exception occurred, it's also None.

**Code Description**: The code first removes three event listeners from the target object – 'after_flush', 'after_commit', and 'after_soft_rollback'. These events are triggered by SQLAlchemy after a flush operation, commit operation, or rollback operation respectively. After these event listeners are removed, the function calls `clear_cache` to reset all three sets that keep track of changes made in a database session. This ensures that only relevant changes are recorded and processed for future reference.

**Note**: The __exit__ method is called automatically when exiting the context manager block using the 'with' statement. It plays an important role in managing resources, such as event listeners or cached data, correctly after they have been used. Without this function, these resources would not be properly cleaned up and could potentially lead to memory leaks or other issues.

**Relationship with Callers**: This function is called internally by the `DBHistory` class when exiting a context manager block using the 'with' statement. It ensures that all event listeners are removed and any cached data is cleared, preventing potential memory leaks or other issues. The __exit__ method also calls `clear_cache` to reset these sets before starting to listen for events again in the next context manager block.

Raw code:```
    def  __exit__(self, type, value, traceback):
        remove_event(self._target, 'after_flush', self._after_flush)
        remove_event(self._target, 'after_commit', self._after_commit)
        remove_event(self._target, 'after_soft_rollback',
                     self._after_rollback)
        self.clear_cache()
```==========

***
### FunctionDef _populate_idents_dict(self, idents, objects)
**_populate_idents_dict**: The function of _populate_idents_dict is to populate an identities dictionary with objects' identity keys. 

**Parameters**:
- idents: This parameter is a dictionary that will be used to store the identities of the objects. It should be initialized before calling this function.
- objects: This parameter is a list of objects for which we want to generate and store their identities in the 'idents' dictionary. 

**Code Description**: The function iterates over all the objects in the provided list, generates an identity key using the `util.identity_key` method (which should return a tuple with two elements), and adds this identity to the corresponding set in the 'idents' dictionary under its first element as the key. If there is no such set yet, it creates one.

**Note**: This function is used internally by `DBHistory` class for tracking changes made to objects during a database session. It helps in maintaining a history of object identities and their corresponding states over time. The 'idents' dictionary can be later used for efficient lookup of an object's state at any given point in the past.

**Relationship with Callers**: This function is called by `_after_commit` method, which is part of `DBHistory` class. It populates identities dictionaries (created_idents, updated_ids, deleted_idents) with objects' identity keys after a database transaction has been committed. These dictionaries are then used for tracking changes made to these objects over time and can be later queried for their states at any given point in the past.

***
### FunctionDef _after_flush(self, db, flush_context, instances)
**_after_flush**: The function of _after_flush is to record changes made during a database flush operation. 

**Parameters**:
- db: This parameter represents the current session object associated with the database.
- flush_context: It holds information about the context in which the flush event was triggered.
- instances (optional): A list of instances that were flushed. If not provided, it defaults to None.

**Code Description**: The function starts by defining a helper function identityset_to_set() that converts an object's members into a set. It then updates three sets: _created, _updated, and _deleted. These sets hold instances of new, dirty, and deleted objects respectively. 

The function is called after each flush event in the database session. The purpose of this function is to keep track of changes made during the flush operation so that they can be undone later if necessary. This feature is particularly useful for testing purposes where you want to verify how your application behaves under different scenarios. 

**Note**: It's important to note that _after_flush() doesn’t actually perform any undo operations, it just records the changes made during a flush operation. To undo those changes, developers need to use other methods provided by SQLAlchemy like rollback().

**Output Example**: The output of this function would be three sets: _created (with new instances), _updated (with dirty instances), and _deleted (with deleted instances). Each set contains unique identifiers for the objects that were created, updated or deleted during the flush operation. 

This function is called by __enter__() method of DBHistory class which listens to 'after_flush' event on the target object. It also calls clear_cache() method to clean up any cached data before starting to listen for events. The __exit__() method cleans up these listeners when it exits the context manager block.

#### FunctionDef identityset_to_set(obj)
**identityset_to_set**: The function of identityset_to_set is to convert an instance of `IdentitySet` into a set. 

**Parameters**: 
- `obj`: An instance of the class `IdentitySet` which represents a collection of identities in a database system.

**Code Description**: This function takes an object (which should be an instance of IdentitySet) as its argument and returns a set containing all values from the members dictionary of that object. The purpose of this is to provide a simple way to convert an `IdentitySet` into a Python set, which can then be used for various purposes such as membership testing or comparison operations.

**Note**: This function assumes that the input object is indeed an instance of IdentitySet and has a _members attribute which is a dictionary-like structure containing identities. If these assumptions are not met, this function may raise unexpected errors. 

**Output Example**: Given an `IdentitySet` with members {'a':1,'b':2}, the output would be a set {1,2}.

***
***
### FunctionDef _after_commit(self, db)
Sure, here is the detailed explanation document for this function:

**_after_commit**: The function of _after_commit is to handle database changes after a successful commit operation. 

**Parameters**: This function takes two parameters:
- db: An instance of SQLAlchemy's `Session` or `Engine` class, representing the current database session or engine.

**Code Description**: The code first checks if the transaction is nested (i.e., it's a part of another transaction). If so, it returns immediately without doing anything as this is unexpected behavior. 

Next, it populates three dictionaries (`self._created`, `self._updated`, and `self._deleted`) with identities of newly created, updated, or deleted objects in the current transaction using the `_populate_idents_dict` method. 

Finally, it calls the `clear_cache` function to reset the sets that keep track of changes made in a database session. This ensures that only relevant changes are recorded and processed for future reference.

**Note**: The `_after_commit` function is part of the SQLAlchemy's event system, which allows applications to hook into various points during the execution of a transaction. In this case, it's being used by the `DBHistory` class to track changes made to objects in a database session and generate identities for these changes.

**Relationship with Callers**: This function is called internally by SQLAlchemy after a successful commit operation. It populates identities dictionaries (created_idents, updated_ids, deleted_idents) with objects' identity keys after a database transaction has been committed. These dictionaries are then used for tracking changes made to these objects over time and can be later queried for their states at any given point in the past.

Raw code:```
    def _after_commit(self, db):
        if db.transaction.nested:
            return
        self._populate_idents_dict(self.created_idents, self._created)
        self._populate_idents_dict(self.updated_idents, self._updated)
        self._populate_idents_dict(self.deleted_idents, self._deleted)
        self.clear_cache()
```==========

***
### FunctionDef _after_rollback(self, db, prev_tx)
Sure, here is the detailed explanation document for this function:

**_after_rollback**: The function of _after_rollback is to reset three sets (`self._created`, `self._updated`, and `self._deleted`) that keep track of changes made in a database session after a rollback operation. 

**Parameters**: This function takes two parameters:
- `db`: The SQLAlchemy database instance. It's used to access the database and perform operations on it.
- `prev_tx`: The previous transaction object. It's used to retrieve information about the changes made in this transaction before the rollback operation.

**Code Description**: After a rollback operation, the function first calls `clear_cache()` to reset all three sets (`self._created`, `self._updated`, and `self._deleted`) that keep track of changes made in a database session. Then it retrieves information about the changes made in this transaction before the rollback operation from the previous transaction object using its methods. After these operations, if there are any changes detected (for example, an object is created, updated, or deleted), their identifiers are added to one of these sets.

**Note**: This function is called by several other functions in the same class (`DBHistory`) after a rollback operation. Specifically, it's called by the following methods: 
- `__exit__`: The `__exit__` method cleans up after exiting the context, calling `_after_rollback` to ensure that no lingering changes are recorded in the session. This function is also called when a commit operation fails and triggers a rollback. In this case, it's used to clear any lingering changes in the session before retrying the commit operation.
- `_after_commit`: This private method is called by SQLAlchemy's event system after a successful commit of a transaction. It populates the `created_idents`, `updated_ids`, and `deleted_idents` dictionaries with identifiers of newly created, updated, or deleted objects in this transaction, and then calls `clear_cache` to clear these identifiers from their respective sets.
- `_after_rollback`: This private method is called by SQLAlchemy's event system after a rollback of a transaction. It simply calls `clear_cache` to clear any lingering changes in the session. 

This function plays an important role in maintaining and tracking database history, ensuring that only relevant changes are recorded and processed.

Raw code:```
    def _after_rollback(self, db, prev_tx):
        self.clear_cache()

```==========
Also, the code has been called by the following objects, their code and docs are as following:
obj: testalchemy.py/DBHistory/__exit__
Document: 
None
Raw code:```
    def __exit__(self, type, value, traceback):
        remove_event(self._target, 'after_flush', self._after_flush)
        remove_event(self._target, 'after_commit', self._after_commit)
        remove_event(self._target, 'after_soft_rollback',
                     self._after_rollback)
        self.clear_cache()

```==========
obj: testalchemy.py/DBHistory/_after_commit
Document: 
None
Raw code:```
    def _after_commit(self, db):
        # ... some codes here ...
        self._after_rollback(db, prev_tx)

```==========

***
