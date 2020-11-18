# Django Bitcoin Field
This is a [Bit](https://pypi.org/project/bit/) implementation on django to have a model field that acts as a Bitcoin wallet. Allowing to send and receive bitcoins transactions. Useful for automated payments.

[Bit Homepage](https://github.com/ofek/bit)

## What is Django Bitcoin Field?

[Bit](https://pypi.org/project/bit/) is a fast and easy library to obtain Bitcoin Wallets that can send/receive bitcoins across the Bitcoin Network. 
These wallets are called **Key**s.
These **keys** can be created and later reused, obtained by a number called **WIF**.

Read more about [**Key**](https://ofek.dev/bit/guide/keys.html) on [Bit docs](https://ofek.dev/bit/).

**Django Bitcoin Field** provide a way to store that **WIF** in the database and retrieve the **Key** object.
**Django Bitcoin Field** doesn't implement any additional methods to the ones provided in  **Key**.


## How to use

### Installation
`pip install django-bitcoin-field`

### Settings
By default, Bitcoin Field will check if **Debug** is enables on django settings to use Bitcoin Testnet Network, allowing to send and receive test payments without any real bitcoin use. Otherwise will use regular Bitcoin Network.
This can be customized adding the next variable in your *settings.py*
```
BIT_NETWORK = True  # This will enable Bitcoin network
BIT_NETWORK = False  # This will enable Bitcoin Test Network
```
If your app have **Debug** enabled only for development and your production server have **Debug** False you dont need to change this setting unless you want to.
A Case Scenario in which you may want a Testnet Key with Debug False is in a staging server that emulates production environments; you will need to use testnet to send and receive transactions for testing purposes. 


### Add to a Model
In your desired *models.py* file, import Bitcoin Field
```
from bit_field.fields import BitcoinField
```
Then in your desired model, add the fields
```
class MyModel(models.Model):
    my_field = BitcoinField()
```
##### Disabling auto generated wallet
By default, Bitcoin Field will auto-create a wallet for every object in your model. If you don't want this behaviour, you could add `default=None` with `null=True`
```
class MyModel(models.Model):
    my_field = BitcoinField(
        default=None,  # Disable auto-default value from BitcoinField
        null=True,  # Enable None values 
        blank=True  # Allow blank on forms/admin site
    )
```

#### Using the Bit Wallet
You can access all [Bit](https://pypi.org/project/bit/) **Key** methods

### Migrating
Once added, you should do the typical `makemigrations` and `migrate`.

### Using the Key
Once a model is created/loaded, if the wif is not None (default behaviour), you will have the **Key** read to use in the **Field**
```
obj = MyModel.objects.get()  # Get some object
obj.my_field  # Key Object
obj.my_field.get_balance()  # Key method to get balance
obj.my_field.get_unspents()  # Key method to get unspents
obj.my_field.any_other_key_method...
```
*Note that you need internet to access Bit APIs.*

## Security
At the moment, django-bitcoin-field is saving WIF as it is on the database as a CharField. 
This is a security issue if you let wallets created by this field with bitcoins on them, since the WIF number itself could be used to retrieve the Key object and send transactions. 
If you need encryption on these fields you can extend BitcoinField and create your custom encryption algorithm overriding the method "get_prep_value(*)".
An optional encryption method will be added in some near future.

## Troubleshooting 

If you get any error, please open an issue and be as much specific as you can, include requirements.txt, python, OS, and any other useful information to help reproduce the issue and fix. 
You can also fork the project, and create a pull request with any fix, I will check it as soon as i can.


## Future Development

### Django Admin

Improve Django Admin to show more information on a Key instead of only showing the wif number.

### Multi Signature

I'm planning to add multi signature support as another field type. 

### Automation Tasks
It's my intention to add some generic tasks and extensible models to quick-enable automated payments.

## Contributions

Code contributions can be done via forking. If you feel like you can do good improvements or have some ideas for this project, send me a message for a Contributor role.
