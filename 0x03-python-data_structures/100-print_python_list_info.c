#include <Python.h>

/**
 * print_python_list_info - function that prints basic info about Python lists
 *
 * @p: A Python Object list.
 */
void print_python_list_info(PyObject *p)
{
	int aa, bb, cc;
	PyObject *dd;

	aa = Py_SIZE(p);
	bb = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", aa);
	printf("[*] Allocated = %d\n", bb);

	for (cc = 0; cc < aa; cc++)
	{
		printf("Element %d: ", cc);

		dd = PyList_GetItem(p, cc);
		printf("%s\n", Py_TYPE(dd)->tp_name);
	}
}
