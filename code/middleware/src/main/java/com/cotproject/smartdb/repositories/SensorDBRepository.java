package com.cotproject.smartdb.repositories;
import jakarta.data.repository.CrudRepository;
import jakarta.data.repository.Repository;
import com.cotproject.smartdb.entities.SensorDB;

import java.util.stream.Stream;
@Repository
public interface SensorDBRepository  extends CrudRepository <SensorDB, String> { // repository containing the methods for interacting with SensorDB entity in mongodb
    Stream<SensorDB> findAll();

}