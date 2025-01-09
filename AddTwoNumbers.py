import cirq
import cirq_google

def createCircuit(qubits):
    circuit = cirq.Circuit()
    
    # example, a=01, b=11
    # apply X (equivalent of NOT) gate to set a and b to their respective values
    circuit.append(cirq.X(qubits[1]))
    circuit.append(cirq.X(qubits[3]))

    # use CNOT (equivalent of XOR) to perform addition of least significant bits
    circuit.append(cirq.CNOT(qubits[0], qubits[4]))
    circuit.append(cirq.CNOT(qubits[1], qubits[4]))

    # use toffoli gate to add carry logic
    circuit.append(cirq.TOFFOLI(qubits[0], qubits[1], qubits[5]))

    # to measure the output of our operation
    circuit.append(cirq.measure(*qubits, key="result"))

    return circuit


def addTwoNumbers():
    """ perform addition of two 2-bit numbers and check if it can be done on quantum chip """
    # create qubits to accomodate the data, we are using 6 qubits - 4 to store no. A and B and 2 to store the sum of A and B
    qubits = [cirq.LineQubit(i) for i in range(6)]
    
    circuit = createCircuit(qubits)

    # get the result of the quantum circuit via simulation, and we do 10 repetitions to get a distribution of result 
    simulator = cirq.Simulator()
    res = simulator.run(circuit, repetitions=10)

    print("Quantum Adder Circuit Result:")
    print(res)

    # now the cool stuff: can this circuit run on any existing Quantum Chips
    try:
        cirq_google.Sycamore.validate_circuit(circuit)
    except Exception as e:
        print(e)


def main():
    """ entry point for the script """
    addTwoNumbers()

if __name__ == "__main__":
    main()