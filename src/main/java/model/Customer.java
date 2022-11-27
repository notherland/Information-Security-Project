package model;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.math.BigDecimal;

/**
 * Simple JavaBean domain object that represents Customer.
 *
 * @author Eugene Suleimanov
 * @version 1.0
 */

@Getter
@Setter
@ToString
public class Customer{

    private String firstName;

    private String lastName;

    private String address;

    private BigDecimal budget;
}