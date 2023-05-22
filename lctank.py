from manim import *

class Inductor(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_shape()

    def create_shape(self):
        # Create custom shape for inductor
        self.set_points_as_corners([ORIGIN, UP, 2 * UP, 3 * UP, 4 * UP])

class Capacitor(VMobject):
    def __init__(self, voltage=0, **kwargs):
        super().__init__(**kwargs)
        self.voltage = voltage
        self.create_shape()

    def create_shape(self):
        # Create custom shape for capacitor
        plate_width = 0.5
        plate_height = 1.5
        gap_height = 0.5
        top_plate = Rectangle(height=plate_height, width=plate_width, stroke_color=WHITE, fill_opacity=0.8)
        bottom_plate = Rectangle(height=plate_height, width=plate_width, stroke_color=WHITE, fill_opacity=0.8)
        gap = Rectangle(height=gap_height, width=plate_width, fill_color=BLACK, fill_opacity=1)
        top_plate.next_to(gap, UP, buff=0)
        bottom_plate.next_to(gap, DOWN, buff=0)

        self.add(top_plate, gap, bottom_plate)

class LCTankCircuit(Scene):
    def construct(self):
        # Parameters
        L = 1  # Inductance (H)
        C = 1  # Capacitance (F)
        R = 0.2  # Resistance (Ω)
        initial_charge = 1  # Initial charge on the capacitor (C)
        initial_current = 0  # Initial current through the inductor (A)
        max_time = 10  # Maximum simulation time (s)
        dt = 0.1  # Time step (s)

        # Circuit components
        inductor = Inductor().shift(UP)
        capacitor = Capacitor().shift(DOWN)
        resistor = Rectangle(height=0.4, width=0.4, fill_color=WHITE, fill_opacity=1).shift(2 * UP)

        # Circuit labels
        inductor_label = Tex("$L$").next_to(inductor, DOWN)
        capacitor_label = Tex("$C$").next_to(capacitor, DOWN)
        resistor_label = Tex("$R$").next_to(resistor, LEFT)

        # Display circuit
        self.play(Create(inductor), Write(inductor_label))
        self.play(Create(capacitor), Write(capacitor_label))
        self.play(Create(resistor), Write(resistor_label))

        # Initial conditions
        charge_label = Tex("$Q(0) = {}$ C".format(initial_charge)).to_corner(UL)
        current_label = Tex("$I(0) = {}$ A".format(initial_current)).to_corner(UL).shift(DOWN)
        self.play(Write(charge_label), Write(current_label))

        # Simulation loop
        charge = initial_charge
        current = initial_current
        time = 0

        while time <= max_time:
            # Update circuit parameters
            voltage = charge / C
            emf = voltage - current * R

            # Update labels
            charge_label_new = Tex("$Q(t) = {:.2f}$ C".format(charge)).to_corner(UL)
            current_label_new = Tex("$I(t) = {:.2f}$ A".format(current)).to_corner(UL).shift(DOWN)
            self.play(Transform(charge_label, charge_label_new), Transform(current_label, current_label_new))

            # Update circuit visual
            capacitor.become(Capacitor(voltage=voltage))
            inductor.become(Inductor(current=current))

            # Update circuit variables
            dcharge_dt = -current
            dcurrent_dt = (emf / L) - (current / (R * C))
            charge += dcharge_dt * dt
            current += dcurrent_dt * dt
            time += dt

            # Pause to observe the animation
            self.wait(dt)

        self.wait(2)  # Pause at the end

