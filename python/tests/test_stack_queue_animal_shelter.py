
def test_enqueue():
    shelter = AnimalShelter()
    dog1 = Dog('Max')
    cat1 = Cat('Luna')
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    assert shelter.dogs[0].name == 'Max'
    assert shelter.cats[0].name == 'Luna'

def test_dequeue():
    shelter = AnimalShelter()
    dog1 = Dog('Max')
    dog2 = Dog('Buddy')
    cat1 = Cat('Luna')
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(dog2)
    assert shelter.dequeue('cat').name == 'Luna'
    assert shelter.dequeue('dog').name == 'Max'
    assert shelter.dequeue('parrot').name == ''

def test_dequeue_failure():
    shelter = AnimalShelter()
    assert shelter.dequeue('cat').name == ''
    assert shelter.dequeue('dog').name == ''
    assert shelter.dequeue('parrot').name == ''

def test_enqueue_failure():
    shelter = AnimalShelter()
    parrot = Animal('Polly')
    shelter.enqueue(parrot)
    assert shelter.dogs == []
    assert shelter.cats == []