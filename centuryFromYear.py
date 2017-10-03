int centuryFromYear(int year) {
    int a;
    if(year%100 == 0){
         a = year/100;
        return a;
    }
    else{
        a = year/100;
        a+=1;
        return a;
    }

}
