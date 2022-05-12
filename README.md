# Running routes visualization
## Related article
https://labdmitriy.github.io/blog/running-routes-visualization

## Functionality
- GPX files parsing
- Routes visualization using OpenStreetMap

## Installation
- Prepare Python environment
- Clone repository
- Navigate to the root project's folder
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```

## Usage example
- Navigate to the root project's folder
- To parse GPX file located in `data/` folder and save the map to the `reports/map.html` file, run the following command:
  ```bash
  python running.py --data data/ --map reports/map.html
  ```
  - All required folders for output file with be created if they don't exist
  - Output file will be opened in the browser after successful command execution
  - Script usage instructions can be displayed with the following command:
    ```bash
    python running.py --help
    ```

## Usage demo
![](./assets/img/usage_example.gif)
