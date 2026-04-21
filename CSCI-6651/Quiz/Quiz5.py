class Elements:
    def __init__(self, label, min_value, max_value):
        self.label = label
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        return self.min_value <= value <= self.max_value
    
def is_float(s):
    if s.count('.') <=1: 
        if s.startswith('-'):
            s = s[1:]
        return s.replace('.', '', 1).isdigit()
    return False

def collect_data(elements):
    results=[]
    while True:
        for i in range(len(elements)):
            element = elements[i]
        while True:
            entry = input(f"Enter {element.label}> ").strip()

            if i == 0 and entry.lower == "q":
                print("Exit")
                return tuple(results)

            if not is_float(entry):
                print("Error. Invalid input. Please enter a floating point number.")
                continue

            value = float(entry)

            if not element.validate(value):
                print("Error, Out of Range")
                continue

            results.append(value)
            break

if __name__ == "__main__":
    elements = [
        Elements("E1", 1.0, 10.0),
        Elements("E2", 2.0, 20.0)
    ]
    result = collect_data(elements)
    print("Final Result:", result)
