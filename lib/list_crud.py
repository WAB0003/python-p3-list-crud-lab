import ipdb 

def create_an_empty_list():
    my_list = list()
    return my_list

def create_a_list():
    my_list = list([1,2,3,4])
    return my_list


def add_element_to_end_of_list(l, element):
    confirmed_list = list(l)
    confirmed_list.append(element)
    return confirmed_list
    

def add_element_to_start_of_list(l, element):
    confirmed_list = list(l)
    confirmed_list.insert(0,element)
    return confirmed_list

def remove_element_from_end_of_list(l):
    confirmed_list = list(l)
    confirmed_list.pop(-1)
    return confirmed_list

def remove_element_from_start_of_list(l):
    confirmed_list = list(l)
    del confirmed_list[0]
    return confirmed_list

def retrieve_first_element_from_list(l):
    confirmed_list = list(l)
    return confirmed_list[0]

def retrieve_element_from_index(l, index):
    confirmed_list = list(l)
    return confirmed_list[index]

def retrieve_last_element_from_list(l):
    confirmed_list = list(l)
    return confirmed_list[-1]
