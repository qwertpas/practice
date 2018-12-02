package org.usfirst.frc.team6036.robot;

import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.VictorSP;


public class Robot extends IterativeRobot {
	

	private Joystick stick = new Joystick(0);
	
	private VictorSP left = new VictorSP(0);
	private VictorSP right = new VictorSP(1);

	

	public void moveJoystick(double x, double y) {
		double driveJoystickYPosition = y;
		double yAxisAlmostScaled = sensCurve(driveJoystickYPosition * 50) * -0.00016;

		double driveJoystickXPosition = x;
		
		double xAxisAlmostScaled = sensCurve(driveJoystickXPosition * 50) * 0.00016;

		double[] inputCoord = new double[2];
        double[] outputCoord = new double[2];

       inputCoord[0] = xAxisAlmostScaled;
       inputCoord[1] = yAxisAlmostScaled;
       outputCoord[0] = 0.0;
       outputCoord[1] = 0.0;
       double[] endCoord = transformMotor(inputCoord, outputCoord);
       double lPower = endCoord[0];
       double rPower = endCoord[1];
       left.setSpeed((-1/0.4) * lPower);
       right.setSpeed((-1/0.4) * rPower);
	}
	
	public double[] transformMotor(double[] coord1, double[] coord2) {
		double max;

		double xAxisScaled = -1 * coord1[0];
		double yAxisScaled = coord1[1];
//		double initY = coord1[1];
		double leftDrive = coord2[0];
		double rightDrive = coord2[1];

        if (Math.abs(xAxisScaled) > Math.abs(yAxisScaled)) {
			max = Math.abs(xAxisScaled);
		} else {
			max = Math.abs(yAxisScaled);
		}

        boolean topRightBottomLeft = (0 <= xAxisScaled &&  xAxisScaled <= max && yAxisScaled == max) || (-max <= xAxisScaled && xAxisScaled <= 0 && yAxisScaled == -max);
        boolean bottomRightTopLeft = (((xAxisScaled == max) && (-max <= yAxisScaled &&  yAxisScaled <= 0)) || ((xAxisScaled == -max) && (0 <= yAxisScaled && yAxisScaled <= max)));
        boolean sides = (((xAxisScaled == max) && (0 <= yAxisScaled &&  yAxisScaled <= 100)) || ((xAxisScaled == -max) && (-max <= yAxisScaled && yAxisScaled <= 0)));
//        		boolean topBottom = (((yAxisScaled == max) && (-max <= yAxisScaled &&  yAxisScaled <= 0)) || ((yAxisScaled == -max) && (0 <= yAxisScaled && yAxisScaled <= max)));

/*
		-----------------------------
		| B						  A	|
		|							|
		|							|
		|							|
		| C						  C	|
		|							|
		|							|
		|							|
		| A						  B	|
		-----------------------------

		A = topRightBottomLeft
		B = bottomRightTopLeft
		C = sides
*/

        if(topRightBottomLeft){
        	leftDrive = yAxisScaled;
        	rightDrive = yAxisScaled - xAxisScaled;
    	} else if(bottomRightTopLeft) {
        	leftDrive = xAxisScaled + yAxisScaled;
        	rightDrive = -1 * xAxisScaled;
    	} else if (sides) {
        	leftDrive = xAxisScaled;
        	rightDrive = yAxisScaled - xAxisScaled;
        } else {
        	leftDrive = xAxisScaled + yAxisScaled;
        	rightDrive = yAxisScaled;
        }

		//////////////////////////
            coord2[0] = leftDrive;
            coord2[1] = rightDrive;


        return coord2;
	}



	@Override
	public void robotInit() {
		
	}
	
	

	@Override
	public void autonomousPeriodic() {
		
	}
	
	@Override
	public void teleopInit() {
		System.out.println("TeleOpInit");
	}
	

	@Override
	public void teleopPeriodic() {
		System.out.println(left.getSpeed() + ", " + right.getSpeed());

		left.feed();
		right.feed();
		left.setSpeed(0.7);
		right.setSpeed(0.7);
		//moveJoystick(stick.getX(), stick.getY());
	}
	
	
	
	
	public double sensCurve(double power) {
		return power * Math.abs(power);
	}
}
