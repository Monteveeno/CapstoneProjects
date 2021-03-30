// I have imported the Scanner so we can allow the user to the enter the details of the project
import java.util.Scanner;

public class projectDetails {

        public static void main(String[] args) {
        //*******Object********
            // we going to use the methods we have given to building objects
            String shapeOfBuilding;
            int amountOfRooms;
            int sizeInMetres;
            int amountOfFloors;
            int expectedBudget;


        // now we are giving our Scanner a variable
        // We going to ask the user various questions about the project
            Scanner building = new Scanner(System.in);

            System.out.println("Please enter the shape of the building: ");
            shapeOfBuilding = building.nextLine();

            System.out.println("How many rooms does the place have: ");
            amountOfRooms = building.nextInt();

            System.out.println("Please enter the size in metres: ");
            sizeInMetres = building.nextInt();

            System.out.println("How many floors do you want there to be: ");
            amountOfFloors = building.nextInt();

            System.out.println("What is your budget for this: ");
            expectedBudget = building.nextInt();

          // now we going to use our to string to print out the results of what the user has give us.
            buildingObject newProject = new buildingObject(shapeOfBuilding, amountOfRooms, sizeInMetres, amountOfFloors, expectedBudget);
            System.out.println(newProject.toString());

            //*******DueDate********
            // we going to use the methods we have given to building objects
            int day;
            int  month;
            int year;

            // now we are giving our Scanner a variable
            // We going to ask the user various questions about the project

            Scanner dueDate = new Scanner(System.in);

            System.out.println("\nNow let's enter due date of this project");

            System.out.println("Please enter the day: ");
            day = dueDate.nextInt();

            System.out.println("Please enter month: ");
            month = dueDate.nextInt();

            System.out.println("Please enter the year: ");
            year = dueDate.nextInt();


            // now we going to use our to string to print out the results of what the user has give us.

            dueDate subMissionDay = new dueDate(day,month, year);
            System.out.println(subMissionDay.toString());


            //*******Amount Paid********
            // we going to use the methods we have given to building objects

            int amountPaid;

            // now we are giving our Scanner a variable
            // We going to ask the user various questions about the project

            Scanner feesPaid = new Scanner(System.in);



            System.out.println("Please enter the amount you have paid so far ");
            amountPaid = feesPaid.nextInt();

            // now we going to use our to string to print out the results of what the user has give us.

            feesPaid outStandingAmount = new feesPaid(amountPaid);
            System.out.println(outStandingAmount.toString());

            //*******Constructor********
            // we going to use the attributes we have given to building objects
            String name;
            String surname;
            String profession;
            int cellPhoneNumber;
            int hourlyWorkRate;

            // now we are giving our Scanner a variable
            // We going to ask the user various questions about the project

            Scanner buildingConstructor = new Scanner(System.in);

            System.out.println("\nNow let's enter the Constructor's Details");

            System.out.println("Please enter the name of the Constructor: ");
            name = buildingConstructor.nextLine();

            System.out.println("Please enter the surname of the Building Constructor: ");
            surname = buildingConstructor.nextLine();

            System.out.println("Please enter the profession: ");
            profession = buildingConstructor.nextLine();


            System.out.println("Please enter the constructor cellphone nuber: ");
            cellPhoneNumber = dueDate.nextInt();

            System.out.println("What is the hourly rate that he charges: ");
            hourlyWorkRate = dueDate.nextInt();

            // now we going to use our to string to print out the results of what the user has give us.

            Constructor constructorDetails = new Constructor(name,surname, profession,cellPhoneNumber,hourlyWorkRate);
            System.out.println(constructorDetails.toString());



        }
}




