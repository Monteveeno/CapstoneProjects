// In this we are creating a object of the amount of fees the customer has paid
// Bellow are the methods we have used
// We will also be initializing this methods by using the the build in function this.
// Then we going to use the toString to print out the results
public class feesPaid {
    int amountPaid;

    public feesPaid(int amountPaid) {
        this.amountPaid = amountPaid;
    }

    public String toString() {
        String output = "The amount customer paid: "+ "R" + amountPaid;


        return output;
    }



}


