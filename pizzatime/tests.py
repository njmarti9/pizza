from django.test import TestCase
from django.db import transaction
from pizzatime.models import Pizza, Topping

# Testing creating new topping
class ToppingTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_making_toppings(self):
        print("\n\nTesting creating new topping:\n")
        pep = Topping.objects.create(name="Pepperoni")
        self.assertTrue(isinstance(pep, Topping))
        self.assertEqual(pep.__str__(), pep.name)
        print(list(Topping.objects.all().values_list('name', flat=True)))

# Testing duplicate toppings
class DupToppingTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_making_dup_toppings(self):
        print("\n\nTesting creating duplicate topping:\n")
        Topping.objects.create(name="Pepperoni")
        try:
            Topping.objects.create(name="Pepperoni")
        except:
            print("Duplicate toppings, can't be made")

class UpdateAndDeleteToppingTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_delete_topping(self):
        print("\n\nTesting updating/deleting new topping:\n")
        print("Creating Pepperoni and Peppers toppings")
        Topping.objects.create(name="Pepperoni")
        Topping.objects.create(name="Peppers")
        print(list(Topping.objects.all().values_list('name', flat=True)))
        print("Updating Pepperoni to Onions")
        Topping.objects.filter(pk=1).update(name='Onions')
        print(list(Topping.objects.all().values_list('name', flat=True)))
        print("Delete 1st topping made")
        Topping.objects.filter(pk=1).delete()
        try:
            # Checks if still an object
            self.assertTrue(Topping.objects.filter(name='Onions').exists())
        except:
            print(list(Topping.objects.all().values_list('name', flat=True)))

class UpdateDuplicateToppingTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_delete_topping(self):
        print("\n\nTesting updating to existing topping:\n")
        print("Creating Pepperoni and Peppers toppings")
        Topping.objects.create(name="Pepperoni")
        Topping.objects.create(name="Peppers")
        print(list(Topping.objects.all().values_list('name', flat=True)))
        print("Updating Pepperoni to Peppers")
        try:
            Topping.objects.filter(pk=1).update(name='Peppers')
        except:
            print("Not Unique, can't update")


class CreatePizzaTestCase(TestCase):
    def setUp(self):
        pass

    def test_pizza(self):
        print("\n\nTesting creating a pizza:\n")
        pep = Topping.objects.create(name="Pepperoni")
        pep.save()
        peppers = Topping.objects.create(name="Peppers")
        peppers.save()
        pizza1 = Pizza.objects.create(specialty="Pepperoni Pizza")
        pizza1.save()
        pizza1.toppings.add(pep)
        print("Pizza1 Name: ", pizza1.specialty.__str__())
        print("Pizza1 toppings: ", pizza1.toppings.all())
        print("Testing creating same named pizza:")
        try:
            with transaction.atomic():
                pizza2 = Pizza.objects.create(specialty="Pepperoni Pizza")
                pizza2.save()
            self.fail('Duplicate pizza made.')
            
        except:
            print("Can't make duplicate pizza")
            pass
        
        print("Testing Updating Pizza and its toppings:")
        pizza1.specialty = "Supreme Pizza"
        pizza1.toppings.add(peppers)
        print("Pizza1 Name: ", pizza1.specialty.__str__())
        print("Pizza1 Toppings: ", pizza1.toppings.all())
        pizza1.toppings.remove(pep)
        print("Pizza1 Toppings: ", pizza1.toppings.all())
        print("Testing adding same toppings:")
        
        try:
            with transaction.atomic():
                pizza1.toppings.add(peppers)
            self.fail('Duplicate topping added.')
            
        except:
            print("Can't add same topping twice")
            pass

        print("Testing deleting pizza: ")
        print("Deleting pizza and its list of toppings:\n", pizza1.delete())
        try:
            with transaction.atomic():
                print("Pizza1 Toppings: ", pizza1.toppings.all())
            self.fail('Pizza does not exist.')
            
        except:
            print("Pizza does not exist")
            pass
        

        
            
        
        

        
