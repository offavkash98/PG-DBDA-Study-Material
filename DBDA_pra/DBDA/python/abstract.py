from abc import abstractmethod,ABC
class RBI(ABC):
    @abstractmethod
    def interest_rate(Self):
        pass

    def new_guideline(self):
        print('3rd party can not save cc details')
        print('for monthly subscriptionm E-madanta')


class SBI(RBI):
    def interest_rate(self):
        print('interestrate  in sbi is 4.7%')

class Axis(RBI):
    def interest_rate(self):
        print('interestrate  in axis is 5.7%')

s=SBI()
s.interest_rate()
s.new_guideline()
    
class Axis(RBI):
    def interest_rate(Self):
        print('interst rate in axisis 3.3')
a = Axis()
a.interest_rate()
a.new_guideline()
