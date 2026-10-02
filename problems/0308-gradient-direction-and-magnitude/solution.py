import numpy as np
def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""

	gradient = np.nan_to_num(np.array(gradient), nan=0.0)

	magnitude = np.linalg.norm(gradient)
	if magnitude == 0:
		direction = np.zeros_like(gradient)
		descent_direction = np.zeros_like(gradient)
	else:
		direction = gradient / magnitude
		descent_direction = -direction
		
	return {
		"magnitude": magnitude,
		"direction": direction,
		"descent_direction": descent_direction
	}