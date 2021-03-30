// In this we are creating a object of the the Architect
// Bellow are the methods we have used
// We will also be initializing this methods by using the the build in function this.
// Then we going to use the toString to print out the results
public class Architect {

        // Attributes
        String name;
        String surname;
        String profession;
        int cellPhoneNumber;
        int hourlyWorkRate;

        // Here we want to enter some arguments for the various information that we want to give
        public Architect (String name, String surname, String profession, int cellPhoneNumber, int hourlyWorkRate) {
            this.name = name;
            this.surname = surname;
            this.profession = profession;
            this.cellPhoneNumber = cellPhoneNumber;
            this.hourlyWorkRate = hourlyWorkRate;

        }

        // toString will help initiatilize the infromation that we want to print out
        public String toString() {
            String output = "Name: " + name;
            output += "\nSurname: " + surname;
            output += "\nProfession: " + profession;
            output += "\nCellPhone Number: " + cellPhoneNumber;
            output += "\nHourly Rate: " + hourlyWorkRate;

            return output;
        }

    }

