/**
 * Autobahn
 * <p>
 * I am a simple command-line application to demonstrate how we create and
 * manipulate Car instances. I also show how we make an application into a real object.
 */
public class Autobahn {

    /**
     * The {@code main} method will be called by the Java VM when we run the application.
     *
     * @param cmdLineArgs We do not use any command-line arguments in the application.
     */
    public static void main( String[] cmdLineArgs ){
        Autobahn application = new Autobahn();
        application.run();
    }

    public void run(){
        Car mikesCar = new Car( "Toyota", "Corolla", "Mike", 312456 );
        Car gumdrop = new Car( "Austin", "Clifton Heavy", "Mr. Hardcastle", 205965 );
        Car herbie = new Car( "Volkswagen", "Beatle", "Disney Studios", 12 );

        System.out.println( "Initial Car Details:" );
        System.out.println( "--------------------" );
        printCarDetails( gumdrop );
        printCarDetails( herbie );
        printCarDetails( mikesCar );

        mikesCar.setOdometer( 212121 );
        gumdrop.setOdometer( 567890 );

        System.out.println( "Updated Car Details:" );
        System.out.println( "--------------------" );
        printCarDetails( gumdrop );
        printCarDetails( herbie );
        printCarDetails( mikesCar );

        printCarDetails( gumdrop );
        printCarDetails( herbie );
        printCarDetails( mikesCar );
    }

    /**
     * A simple method to print the details of any Car instance to the system output stream.
     * @param aCar A Car instance.
     */
    private void printCarDetails( Car aCar ){
        System.out.println( "Make:      " + aCar.getManufacturer() );
        System.out.println( "Model:     " + aCar.getModel() );
        System.out.println( "Owner:     " + aCar.getOwner() );
        System.out.println( "Odometer:  " + aCar.getOdometer() );
        System.out.println();
    }
}