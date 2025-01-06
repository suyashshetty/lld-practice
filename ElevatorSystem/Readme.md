# Elevator System

## Step 1: Requirements Analysis

### Functional Requirements

- **Basic Movement**: Two elevators (A and B) that move up and down.
- **External Requests**: Users can request an elevator at any floor using an external button (up/down).
- **Internal Requests**: Users can request to go to any floor using internal buttons.
- **Stop at Requested Floors**: Elevators stop at requested floors.
- **Priority Handling**: Elevators use different strategies to handle multiple requests.
- **Arrival Notification**: Elevators alert users when they reach the requested floor.

### Safety Requirements

- **Weight Monitoring**: Elevators warn and pause if weight exceeds 90% of capacity.
- **Abnormal Operation**: Elevators pause and display alerts during abnormal operations.
- **Reserve Mode**: Serve a single floor exclusively for a time period.
- **Maintenance Mode**: Cease operations for repairs.

### Emergency Requirements

- **Manual Override**: Allow doors to be opened externally during emergencies.
- **Emergency Brakes**: Stop and hold in case of power loss or emergencies.
- **Fire/Emergency Protocol**: Handle fire and emergency scenarios safely.

### Display and Communication

- **Floor Display**: Show current elevator position and direction outside each floor.

# Non-Functional Requirements for Elevator System

## 1. Efficiency
- Elevators should be efficient in **power management** and **time management**.
- In case of a tie, **prioritize time management** over power management.

## 2. Usability
- Elevators should have **intuitive button design** and easy-to-use navigation.
- Buttons should include **Braille markings** and **audible feedback** for accessibility.

## 3. Monitoring and Logging
- The system should have a **monitoring system** to log and analyze:
  - Power supply usage.
  - Weight inside the elevator.
  - Movement and operational status.

## 4. Safety Standards
- Elevators must comply with **ISO safety standards**.
- A **fire extinguisher** should be installed in each elevator for fire safety.
- Conduct periodic safety drills and equipment inspections.
- Elevators should have a ventilation system to ensure air circulation inside the cabin for user comfort and safety.

## 5. Maintainability and Upgradability
- Elevators should be easily maintainable with modular parts for repairs or upgrades.
- Software should support upgrades to incorporate **different strategies** based on usage or requirements.

## 6. Alerts and Notifications
- Elevators should alert users in the following scenarios:
  - **Overweight condition**.
  - **Door open** for too long.
  - **Abnormal operations** (e.g., sensor/motor issues).

## 7. Energy Efficiency
- Elevators should consume **minimal power** when idling at any floor.
- Use energy-saving modes like standby lighting and regenerative braking systems.

## 8. Emergency Handling
- Elevators should have a **power backup system** capable of safely grounding the elevator to the base floor during a power outage.
- **Emergency brakes** must be deployed to stop and hold in emergencies.
- Include a **manual override** mechanism for external door opening during fire/emergency.

# Core Entities
- Button
- Door
- Elevator
- Floor
- Light
- Emergency Brake
- Controller
- Weight Sensor
- Display
- Power Backup
