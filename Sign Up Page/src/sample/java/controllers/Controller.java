package controllers;

import javafx.event.ActionEvent;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;

public class Controller implements Initializable {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private VBox rootVBox;

    @FXML
    private StackPane rootStackPane;

    @FXML
    private Label nameLabel1;

    @FXML
    private Label nameLabel;

    @FXML
    private TextField nameTextField;

    @FXML
    private Label emailLabel;

    @FXML
    private TextField emailTextField;

    @FXML
    private Label genderLabel;

    @FXML
    private HBox genderRadioPane;

    @FXML
    private RadioButton femaleRadio;

    @FXML
    private ToggleGroup genderToggleGroup;

    @FXML
    private RadioButton maleRadio;

    @FXML
    private Label passwordLabel;

    @FXML
    private PasswordField passwordField;

    @FXML
    private Label confirmPasswordLabel;

    @FXML
    private PasswordField confirmPasswordField;

    @FXML
    private ButtonBar buttonBar;

    @FXML
    private Button signupButton;

    @FXML
    private void signUpEvent(ActionEvent event){
        if(nameTextField.getText().isEmpty()||
                emailTextField.getText().isEmpty()||
                passwordField.getText().isEmpty()||
                confirmPasswordField.getText().isEmpty()){
            showInfo("Error","Ensure all fields are filled up","Empty fields");

        }

        else{
            if(passwordField.getText() != confirmPasswordField.getText()){
                showInfo("Error","The passwords do not match","Passwords must match");
            }
            else{
                showInfo("Success","","Sign in Successful");
            }
        }
    }
    private void showInfo(String title, String body, String header){
        Alert alert  = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(header);
        alert.setContentText(body);
        alert.show();
    }
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
    }

}
