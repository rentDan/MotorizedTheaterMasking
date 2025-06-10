"""
The problem

Projector screens are designed in various aspect ratios, and movies
are produced in various aspect ratios. A screen may handle certain aspect 
ratio better than others. For example, if you had a screen near the 16:9 
ratio(shape closer to a square), and you were watching a movie in 2:39:1(closer
to a rectangle), the picture would fit from left to right but not from top to 
bottom. This would leave unused space above and below the picture, and with 
a projector, that would cause light to be reflected off of that space, leaving 
gray bars that can distract and actually dull the contrast of the movie.

Project Ideals

A motor is being controlled by a user. The motor moves in steps, in which
each step is a degree of rotation in a given direction (clockwise/c-clockwise).
It will be pulling horizontal panels either closer together or further apart.

Steps will be used as the tracking system for the panels. Zero steps will
refer to the state of the curtains being fully open. Max steps will refer
to the state of the curtains being as close as the smallest aspect ratio.
At zero, the distance between the shades is greatest.
At max, the distance between the shades is smallest.

The user will be able to control the position of the shades through a webpage.
The webpage will contain two main features: preset positions and manual movement.

Preset positions allow the user to set the shades to a desired
position via a specified aspect ratio. Each aspect ratio will be saved as
a constant. The constant will refer to the amount of steps needed to reach
that position in relation to reset, i.e., from zero how many steps are needed
to reach the position.

Manual Movement allows the user to move the shades by holding either an up
or down button. They will be able to use this feature regardless of the shade's
position.

The main problem is these two features coinciding. I will have to make sure
that one feature does not disrupt the other. This will be handled in the as
seen in the code below.
"""


#Variables
max_steps: int #widest aspect ratio
steps_taken: int #from reset

#Constant Position Variables - steps to position from reset - reset being 0
TWO_THIRTY_NINE: int #most common wide
SIXTEEN_NINE: int #reset aspect ratio
#More to come

#Functions
def reset(steps_currently: int) -> int:
    """
    Sets the position of the shades back to fully open by
    calculating how many steps are needed to reach it.
    
    Parameters:
    - steps_currently (int): [steps_taken] Steps needed to reach reset.
    
    Returns:
    int: Expected 0 as this will be the new steps_taken value 
            after the shade is moved. If loop breaks early steps_taken
            should still be accurate.
            
    Examples:
    # Example 1:
    steps_taken = reset(steps_taken)
    """ 
    steps_currently = 0 #to be removed on implementation
    return steps_currently

def position(aspect_ratio: int, steps_currently: int) -> int:
    """
    Moves the shades to a specified aspect ratio.
    
    Parameters:
    - aspect_ratio (int):    One of the constant variables that holds the amount
                             of steps needed to reach a position from reset.
    - steps_currently (int): [steps_taken] Current steps from reset.
    
    Returns:
    int: New value of steps_currently after shade is moved.
    
    Examples:
    # Example 1:
    steps_taken = position(TWO_THIRTY_NINE, steps_taken)
    """
    #steps_remaining: int will be used here to calculate steps until position reached
    
    #value of steps currently will be new steps_taken from reset.
    steps_currently = 0 #to be removed on implementation
    return steps_currently

def manual(direction: bool, steps_to_take: int, steps_currently: int) -> int:
    """
    Manual movement of the motor, issued by user moving a slider to the amount of
    steps they want to take, then pressing direction.
    
    Parameters:
    - direction (bool): Either 'up' or 'down'.
    - steps_currently (int): [steps_taken] Current steps from reset.
    - steps_to_take (int): The number of steps the motor should move.
    
    Returns:
    int: New value of steps_currently after shade is moved.
    
    Examples:
    # Example 1:
    steps_taken = manual(direction_got, steps_taken, steps_to_take)
    """
    steps_currently = 0 #to be removed on implementation
    return steps_currently
