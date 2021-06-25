const fs=require('fs');
const path=require('path');

let testFolder= 'E:\\';
let mainArray=[];

console.log(1);
console.log(2);

var cnt=0;

var obj={
    table:[]
};

async function main(testFolder){
    var initial_date=new Date().getTime();

    fs.readdir(testFolder,(err,files)=>{
        files.forEach(file=>{
            const absolutePath = path.resolve(testFolder,file)
            console.log(file, path.parse(absolutePath));
            obj.table.push({
                name:file,
                path:path.parse(absolutePath),
            });
            cnt+=1
            fs.stat(absolutePath,(err,stats)=>{
                if(err){
                    return;
                }
                if(stats.isDirectory()){
                    main(absolutePath);
                }
            })
        });
        var json=JSON.stringify(obj);
    
        fs.writeFile('drive-e.json',json,'utf8',(err)=>{
            if(err){
                return;
            };
        });
        var final_date=new Date().getTime();
        var time_diff=Math.abs(final_date-initial_date)/(1000*60);
        console.log("************************");
        console.log(" ");
        console.log(String(cnt)+"Files Indexed in "+ String(time_diff)+" min");
        console.log(" ");
        console.log("************************");
    });

}

main(testFolder);

console.log(3);
console.log(4);

