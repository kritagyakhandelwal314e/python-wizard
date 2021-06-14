class SuperList(list):
  def __len__(self):
    return 1000


super_list1 = SuperList()
print(len(super_list1))
super_list1.append(1)
super_list1.extend([2, 3, 4, 5, 6, 7, 8])
print(super_list1)
print(super_list1[4])
print(len(super_list1))
print(issubclass(SuperList, list))
print(issubclass(list, object))
