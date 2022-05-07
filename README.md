[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Sensor Data ELT</h3>

  <p align="center">
    A fully dockerized ELT pipeline project, using Postgres, MYSQL, dbt, Apache Airflow,  Redash and Superset.
    <br />
    <a href="https://sensor-data-elt.herokuapp.com/index.html#!/overview"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering">View Demo</a>
    ·
    <a href="https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/issues">Report Bug</a>
    ·
    <a href="https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A fully dockerized using a docker-compose file ELT pipeline using MySQL, PostgreSQL, Airflow, DBT, Redash and Superset. used MySQL and Postgres for data ware house. used DBT for data transforming and airflow for automation and orchestrations. A redash and Superset dasboard is built by connecting it to our data ware .
### Built With

Tech Stack used in this project
* [Postgres](https://www.postgresql.org/)
* [MYSQL](https://www.mysql.com/)
* [Apache Airflow](https://airflow.apache.org/)
* [dbt](https://www.getdbt.com/)
* [Redash](https://redash.io/)
* [Superset](https://superset.apache.org/)



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering.git
   ```
2. Run
   ```sh
    docker-compose build
    docker-compose up
   ```
3. Open Airflow web browser
   ```JS
   Navigate to `http://localhost:8000/` on the browser
   activate and trigger load_data dag
   activate and trigger migrate_data dag
   activate and trigger dbt_dbt_dag
   ```
4. Access your Postgres database using adminar
   ```JS
   Navigate to `http://localhost:8080/` on the browser
   use `postgres` databse
   use `postgres-dbt` server
   use `dbtuser` for username
   use `pssd` for password
   ```
5. Access redash dashboard
   ```sh
   open new terminal
   docker-compose run — rm server create_db
   Open pstgres-dbt using adminar
   Create a user for analytics database
   CREATE USER 'redash'@'' IDENTIFIED WITH mysql_native_password BY 'root';
   Grant all privilages for analytics database
   GRANT ALL PRIVILEGES ON analytics.* To 'redash'@'';
   ```
   ```JS
   Navigate to `http://localhost:5000/` on the browser
   Login and use your created user on analytics databse to connect to your databse
   ```
6. Access Superset dashboard
   ```JS
   Navigate to `http://localhost:8088/` on the browser
   use `root` for username
   use `roor` for password
   ```
  

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

    Binyam Sisay - binasisayet8790@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [10 Academy](https://www.10academy.org/)
* Daniel Zelalem



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Bina-man/Sensor_data_ETL-ELT_DataEngineering.svg?style=for-the-badge
[contributors-url]: https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Bina-man/Sensor_data_ETL-ELT_DataEngineering.svg?style=for-the-badge
[forks-url]: https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/network/members
[stars-shield]: https://img.shields.io/github/stars/Bina-man/Sensor_data_ETL-ELT_DataEngineering.svg?style=for-the-badge
[stars-url]: https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/stargazers
[issues-shield]: https://img.shields.io/github/issues/Bina-man/Sensor_data_ETL-ELT_DataEngineering.svg?style=for-the-badge
[issues-url]: https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/issues
[license-shield]: https://img.shields.io/github/license/Bina-man/Sensor_data_ETL-ELT_DataEngineering.svg?style=for-the-badge
[license-url]: https://github.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/bina3c
[product-screenshot]: https://raw.githubusercontent.com/Bina-man/Sensor_data_ETL-ELT_DataEngineering/main/images/design.png


