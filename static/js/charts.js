function renderBloodChart(data){

const ctx = document.getElementById('bloodChart');

const normalizedData = [
data[0],        // Hemoglobin
data[1]*10,     // RBC scaled
data[2]/10000,  // Platelets scaled
data[3],
data[4],
data[5],
data[6]
];

new Chart(ctx,{
type:'bar',
data:{
labels:[
'Hemoglobin',
'RBC (x10)',
'Platelets (/10000)',
'MCV',
'MCH',
'MCHC',
'PDW'
],
datasets:[{
label:'Blood Values',
data:normalizedData,
backgroundColor:[
'#ff6384',
'#36a2eb',
'#ffcd56',
'#4bc0c0',
'#9966ff',
'#ff9f40',
'#8bc34a'
]
}]
},
options:{
responsive:true
}
});
}