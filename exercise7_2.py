from itertools import chain


class Employee:
    def __init__(self) -> None:
        self.busy = False

    def __bool__(self) -> bool:
        return self.busy

    def __str__(self) -> str:
        return "ox"[self.busy]

    def assign_call(self) -> None:
        self.busy = True


class Respondent(Employee):
    pass


class Manager(Employee):
    pass


class Director(Employee):
    pass


class CallCenter:
    def __init__(self, nr: int, nm: int, nd: int) -> None:
        self.respondents = [Respondent() for _ in range(nr)]
        self.managers = [Manager() for _ in range(nm)]
        self.directors = [Director() for _ in range(nd)]

    def __str__(self) -> str:
        sr = "respondents: " + "".join(str(e) for e in self.respondents)
        sm = "   managers: " + "".join(str(e) for e in self.managers)
        sd = "  directors: " + "".join(str(e) for e in self.directors)
        return f"{sr}\n{sm}\n{sd}"

    def dispatch_call(self) -> Employee:
        employees = chain(self.respondents, self.managers, self.directors)
        for e in employees:
            if not e:
                e.assign_call()
                return e
        raise MemoryError("No employee available")
