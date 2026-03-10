package wethinkcode.cars.v3;

import java.awt.*;
import java.time.Year;

public class Car {
    private String manufacturer;
    private String model;
    private Year year;
    private Color colour;
    private int kmReading;

    public Car( String manufacturerName, String modelName, Year modelYear, Color carColour ){
        manufacturer = manufacturerName;
        model = modelName;
        year = modelYear;
        colour = carColour;
        kmReading = 0;
    }

    public String getManufacturer(){
        return manufacturer;
    }

    public String getModel(){
        return model;
    }

    public Year getYear(){
        return year;
    }

    public Color getColour(){
        return colour;
    }

    public void setColour( Color aNewColour ){
        colour = aNewColour;
    }

    public int getKm(){
        return kmReading;
    }

    public void addKm( int kmTravelled ){
        if( kmTravelled < 0 ) return;
        kmReading += kmTravelled;
    }

    public String asFormattedString(){
        return "Make:   " + getManufacturer() + '\n'
            + "Model:  " + getModel() + '\n'
            + "Year:   " + getYear() + '\n'
            + "Colour: " + getColour() + '\n';
    }
}