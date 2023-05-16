#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to python object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	int i;
	PyListObject *list = (PyListObject *)p;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
