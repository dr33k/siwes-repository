
import java.util.EmptyStackException;
import java.util.Scanner;
import java.util.Stack;
import java.lang.Double;

public class EvaluateExpressions{
    public static String number = "";
    public static boolean recursion = false;
    private static Stack<String> operandStack = new Stack();
    private static Stack<Character> operatorStack = new Stack();

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        input = "("+input+")";

        for(int i = 0;i< input.length();i++){
            evaluate(input.charAt(i));
        }

        System.out.println(operandStack.peek());
    }

    public static void evaluate(Character token){

        if (Character.isDigit(token)){ number+= String.valueOf(token); return;}
        else{
            //If operator, push last number into operand stack and clear it
            operandStack.push(number);  number ="";
            //Remove all empty strings in operand stack
            while(operandStack.contains("")){operandStack.removeElement("");}

            try {
                performOperation(token);
            }
            catch (EmptyStackException ex){
                System.out.println("Operator stack empty");
            }
            finally{
                //Push operator
                if (token != ')') operatorStack.push(token);
                return;
            }
        }
    }
    public static char performOperation(char nextOperator) throws EmptyStackException {
        /**This method performs binary operations and does it in a way that there are no more
         * than two operands in the operandStack UNLESS in the event of an '*' or '/'
         */

        //Peek at the last operator inserted
        char precedingOperator = operatorStack.peek();

        //If there are enough operands to work with
        if (operandStack.size() > 1 ) {

            if (nextOperator == '+') {
                if (recursion) {
                    addPush();
                    /**
                     * In the case of the backward recursive process of searching for an '(' when an ')' is found, let it perform
                     * the same operation as the updated 'nextOperator'. NOTE: In backward recursion nextOperator for the next
                     * recursive process is the current preceding operator. The one at the top of the stack AFTER an executed operation.
                     **/
                    //Continue recursion
                    precedingOperator = performOperation(operatorStack.peek());
                } else {//Under non-recursive (default code execution) circumstances
                    switch (precedingOperator) {
                        case '+':
                            addPush();
                            break;
                        case '-':
                            subtractPush();
                            break;
                        case '*':
                            multiplyPush();
                            break;
                        case '/':
                            dividePush();
                            break;
                        default:
                            break;
                    }
                }
            } else if (nextOperator == '-') {
                if (recursion) {
                    subtractPush();
                    //Continue recursion
                    precedingOperator = performOperation(operatorStack.peek());
                } else {
                    switch (precedingOperator) {
                        case '+':
                            addPush();
                            break;
                        case '-':
                            subtractPush();
                            break;
                        case '*':
                            multiplyPush();
                            break;
                        case '/':
                            dividePush();
                            break;
                        default:
                            break;
                    }
                }
            } else if (nextOperator == '*') {
                if (recursion) {
                    multiplyPush();
                    //Continue recursion
                    precedingOperator = performOperation(operatorStack.peek());
                } else {
                    switch (precedingOperator) {
                        /**
                         * The '+' and '-' cases are implemented to respect the priority that '*' has over them.
                         * Hence, no operation will be performed and this function will return and wait for the next
                         * operand which will then multiply the preceding operand
                         **/
                        case '+':
                        case '-':
                            return precedingOperator;
                        case '*':
                            multiplyPush();
                            break;
                        case '/':
                            dividePush();
                            break;
                        default:
                            break;

                    }
                }
            } else if (nextOperator == '/') {
                if (recursion) {
                    dividePush();
                    //Continue recursion
                    precedingOperator = performOperation(operatorStack.peek());
                } else {
                    switch (precedingOperator) {
                        /**
                         * The '+' and '-' cases are implemented to respect the priority that '/' has over them.
                         * Hence, no operation will be performed and this function will return and wait for the next
                         * operand which will then divide the preceding operand
                         **/
                        case '+':
                        case '-':
                            return precedingOperator;
                        case '*':
                            multiplyPush();
                            break;
                        case '/':
                            dividePush();
                            break;
                        default:
                            break;
                    }
                }
            }
        }
        //This else-if branch is responsible for ending the recursion if any. It assumes '(' has been reached.
        // It is outside the first if statement of this method
        if(nextOperator == '(' && recursion  ) {removeOpeningBracket();System.out.println("Recursion ended"); recursion = false;}

        //This else-if branch is responsible for beginning the recursion. It assumes nextOperator == ')'
        else if(nextOperator == ')'){ recursion = true;
        precedingOperator = performOperation(operatorStack.peek());
        }

        return precedingOperator;
    }


    public static void addPush(){
        System.out.println(operandStack);System.out.println(operatorStack);
        operatorStack.pop(); //Remove the add operator
        double num2 = Double.parseDouble(operandStack.pop());
        double num1 = Double.parseDouble(operandStack.pop());
        operandStack.push(String.valueOf(num1+ num2));
        System.out.println(operandStack);System.out.println(operatorStack);}
    public static void subtractPush(){
        System.out.println(operandStack);System.out.println(operatorStack);
        operatorStack.pop(); //Remove the subtract operator
        double num2 = Double.parseDouble(operandStack.pop());
        double num1 = Double.parseDouble(operandStack.pop());
        operandStack.push(String.valueOf(num1- num2));
        System.out.println(operandStack);System.out.println(operatorStack);}
    public static void multiplyPush(){
        System.out.println(operandStack);System.out.println(operatorStack);
        operatorStack.pop(); //Remove the multiply operator
        double num2 = Double.parseDouble(operandStack.pop());
        double num1 = Double.parseDouble(operandStack.pop());
        operandStack.push(String.valueOf(num1* num2));
        System.out.println(operandStack);System.out.println(operatorStack);}
    public static void dividePush(){
        System.out.println(operandStack);System.out.println(operatorStack);
        operatorStack.pop(); //Remove the divide operator
        double num2 = Double.parseDouble(operandStack.pop());
        double num1 = Double.parseDouble(operandStack.pop());
        operandStack.push(String.valueOf(num1/ num2));
        System.out.println(operandStack);System.out.println(operatorStack);}
    public static void removeOpeningBracket(){ System.out.println(operandStack);System.out.println(operatorStack);operatorStack.pop(); System.out.println(operandStack);System.out.println(operatorStack);}
}