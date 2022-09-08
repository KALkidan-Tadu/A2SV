class MyCircularDeque {
public:
    int size=0, front=0, rear=-1, maxsize;
    int * q;
    MyCircularDeque(int k) {
        q = new int[k];
        maxsize = k;
    }
    bool insertFront(int value) {
        if(isFull())
            return false;
        front = (front - 1 + maxsize) % maxsize;
        q[front] = value;
        size++;
        if(rear == -1)
            rear = front;
        return true;
    }
    
    bool insertLast(int value) {
        if(isFull())
            return false;
        rear = (rear + 1) % maxsize;
        if(size == 0)
            front = rear;
        q[rear] = value;
        size++;
        return true;
    }
    
    bool deleteFront() {
       if(isEmpty())
           return false;
        front = (front + 1) % maxsize;
        size--;
        return true;
    }
    
    bool deleteLast() {
        if(isEmpty())
            return false;
        rear = (rear - 1 + maxsize) % maxsize;
        size--;
        return true;
    }
    
    int getFront() {
        if(isEmpty())
            return -1;
        return q[front];
    }
    
    int getRear() {
        if(isEmpty())
            return -1;
        return q[rear];
    }
    
    bool isEmpty() {
        return size==0;
    }
    
    bool isFull() {
        return size==maxsize;
    }
};
