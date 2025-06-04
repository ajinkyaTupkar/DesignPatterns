package personal.DesignPatterns.creational;

public class Singleton {
    // Private static instance of the class
    private static Singleton instance;

    // Private constructor to prevent instantiation
    private Singleton() {}

    // Public method to provide access to the instance
    // SYNCHRONIZED - to ensure thread safety
    // public static synchronized Singleton getInstance() {  (This is suboptimal as it locks the method every time it's called, even after the instance is created)
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {  // Synchronized is used here to block only if instance is null this is a minor optimization. Synchronized can be used in method as well. But that will increase latency.
                if (instance == null) { // Double-checked locking
                    // Check again to ensure that only one instance is created
                    // Lazy initialization
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
       

    // Example method
    public void showMessage() {
        System.out.println("Hello from Singleton!");
    }

    public static void main(String[] args) {
        // Get the single instance of the class
        Singleton singleton = Singleton.getInstance();
        singleton.showMessage();
    }
}