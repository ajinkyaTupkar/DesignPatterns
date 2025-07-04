package creational.abstractfactory;

// Abstract Product A
interface Chair {
    void sitOn();
}

// Concrete Product A1
class VictorianChair implements Chair {
    @Override
    public void sitOn() {
        System.out.println("Sitting on a Victorian Chair.");
    }
}

// Concrete Product A2
class ModernChair implements Chair {
    @Override
    public void sitOn() {
        System.out.println("Sitting on a Modern Chair.");
    }
}

// Abstract Product B
interface Sofa {
    void lieOn();
}

// Concrete Product B1
class VictorianSofa implements Sofa {
    @Override
    public void lieOn() {
        System.out.println("Lying on a Victorian Sofa.");
    }
}

// Concrete Product B2
class ModernSofa implements Sofa {
    @Override
    public void lieOn() {
        System.out.println("Lying on a Modern Sofa.");
    }
}

// Abstract Factory
interface FurnitureFactory {
    Chair createChair();
    Sofa createSofa();
}

// Concrete Factory 1
class VictorianFurnitureFactory implements FurnitureFactory {
    @Override
    public Chair createChair() {
        return new VictorianChair();
    }

    @Override
    public Sofa createSofa() {
        return new VictorianSofa();
    }
}

// Concrete Factory 2
class ModernFurnitureFactory implements FurnitureFactory {
    @Override
    public Chair createChair() {
        return new ModernChair();
    }

    @Override
    public Sofa createSofa() {
        return new ModernSofa();
    }
}

// Client
public class AbstractFactoryExample {
    public static void main(String[] args) {
        FurnitureFactory victorianFactory = new VictorianFurnitureFactory();
        Chair victorianChair = victorianFactory.createChair();
        Sofa victorianSofa = victorianFactory.createSofa();

        victorianChair.sitOn();
        victorianSofa.lieOn();

        FurnitureFactory modernFactory = new ModernFurnitureFactory();
        Chair modernChair = modernFactory.createChair();
        Sofa modernSofa = modernFactory.createSofa();

        modernChair.sitOn();
        modernSofa.lieOn();
    }
}