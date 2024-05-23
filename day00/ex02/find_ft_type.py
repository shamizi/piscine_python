def all_thing_is_obj(object: any) -> int:
   # print(type(object))
    obj = type(object)
    if (isinstance(object, list)):
        print("List :", obj)
    elif (isinstance(object, tuple)):
        print("Tuple :", obj)
    elif (isinstance(object, set)):
        print("Set :", obj)
    elif (isinstance(object, dict)):
        print("Dict :", obj)
    elif (isinstance(object, str)):
        print( object, "is in the kitchen :", obj)
    else:
        print ("Type not found")
    return 42