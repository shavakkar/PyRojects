from phonenumbers import geocoder, carrier,timezone
import phonenumbers

phone = input("Enter the Number with country code: ")
phoneNumber = phonenumbers.parse(phone)

country_name = geocoder.description_for_number(phoneNumber,'en')

serviceProvider = carrier.name_for_number(phoneNumber,'en')

timeZone = timezone.time_zones_for_number(phoneNumber,'en')

print(country_name)
print(serviceProvider)
print(timeZone)
