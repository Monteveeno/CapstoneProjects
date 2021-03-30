// In this we are creating a object of the dueDate
// Bellow are the methods we have used
// We will also be initializing this methods by using the the build in function this.
// Then we going to use the toString to print out the results
public class dueDate {
    int day;
    int month;
    int year;


    // Here we want to enter some arguments for the various information that we want to give
    public dueDate(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;

    }
    public String toString() {
        String output = "Day: " + day;
        output += "\nMonth: " + month;
        output += "\nYear: " + year;

        return output;
    }
}
