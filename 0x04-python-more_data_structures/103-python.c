#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - prints python list
 * @p: Python Object
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	int i;
	PyListObject *list = (PyListObject *)p;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %d: %s\n", i, typeName);
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: Python Object
 *
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	(void)p;
}
