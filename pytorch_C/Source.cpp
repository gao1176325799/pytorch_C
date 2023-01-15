#include <torch/torch.h>
#include <iostream>
#include <pybind11/pybind11.h>
namespace py = pybind11;
void readtorch(torch::Tensor t);

int main() {
	torch::Tensor tensor = torch::rand({ 2, 3 });
	std::cout << typeid(tensor).name()<<"\n";
	readtorch(tensor);
	std::cin.get();
}
void readtorch(torch::Tensor t) {
	std::cout << "calling C Success, the data input type is:";
	std::cout << typeid(t).name() << "\n";
}

PYBIND11_MODULE(example1, m) {
	m.doc() = "pybind11 read torch test";
	m.def("readtorch", &readtorch, "A function read torch datatype");
}