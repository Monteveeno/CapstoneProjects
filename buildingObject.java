// In this we are creating a object of the building
// Bellow are the methods we have used
// We will also be initializing this methods by using the the build in function this.
// Then we going to use the toString to print out the results

public class buildingObject {
    String shapeOfBuilding;
    int amountOfRooms;
    int sizeInMetres;
    int amountOfFloors;
    int expectedBudget;

    public buildingObject (String shapeOfBuilding, int amountOfRooms, int sizeInMetres, int amountOfFloors, int expectedBudget) {
        this.shapeOfBuilding = shapeOfBuilding;
        this.amountOfRooms = amountOfRooms;
        this.sizeInMetres = sizeInMetres;
        this.amountOfFloors = amountOfFloors;
        this.expectedBudget = expectedBudget;
    }
    // toString will help initiatilize the infromation that we want to print out
    public String toString() {
        String output = "Shape is: " + shapeOfBuilding;
        output += "\nAmount of rooms is: " + amountOfRooms;
        output += "\nThe overall size of the building is: " + sizeInMetres;
        output += "\nAmount of floors: " + amountOfFloors;
        output += "\nThe budget for this is: "+ "R" + expectedBudget;

        return output;
    }
}
