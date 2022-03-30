package com.schooldevops.ssm.secretsmanager;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Component;

@Component
@SpringBootApplication
public class SecretsManagerApplication implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(SecretsManagerApplication.class, args);
	}

	@Value("${dbname}")
	private String dbname;

	@Value("${test.value}")
	private String testValue;

	@Value("${api.password}")
	private String api_password;

	@Value("${db.db-host}")
	private String db_host;

	@Override
	public void run(String... args) throws Exception {
		System.out.println("DBName: " + dbname + " : " + testValue + " apiPassword: " + api_password + " : db_host: " + db_host);
	}
}
