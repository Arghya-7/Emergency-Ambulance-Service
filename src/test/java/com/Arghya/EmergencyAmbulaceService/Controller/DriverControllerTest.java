package com.Arghya.EmergencyAmbulaceService.Controller;

import com.Arghya.EmergencyAmbulaceService.Entity.Driver;
import com.Arghya.EmergencyAmbulaceService.controller.DriverController;
import com.Arghya.EmergencyAmbulaceService.service.DriverServices;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.util.List;

import static org.mockito.Mockito.when;

public class DriverControllerTest {
    @Mock
    DriverServices driverServices;

    DriverController driverController;

    @BeforeEach
    public void setUp(){
        MockitoAnnotations.openMocks(this);
        this.driverController = new DriverController(driverServices);
    }

    @Test
    public void testFindAllMethod() {
        when(driverServices.displayAll())
                .thenReturn(List.of(new Driver()));
        Assertions.assertTrue(driverController.displayAllDriver().size() > 0);
    }
}
