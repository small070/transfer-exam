import pyttsx3
import time

engine = pyttsx3.init()

txt = ['assemble', 'assembly line', 'automated', 'batch', 'component', 'conveyor belt', 'customize'
       , 'defect', 'device', 'electronics', 'examine', 'facility', 'gadget', 'glitch', 'in stock', 'in-house'
       , 'inspect', 'install', 'inventory', 'launch', 'machinery', 'maintenance', 'malfunction', 'manufacturer'
       , 'mechanic', 'model', 'on-site', 'output', 'outsource', 'overproduction', 'packaging', 'patent', 'plant'
       , 'procedure', 'product line', 'production', 'quality control', 'raw material', 'recall', 'shortage'
       , 'shut down', 'strike', 'subcontract', 'warehouse', 'wholesale']
i = 0
while True:
       engine.say(txt[i])
       engine.runAndWait()
       time.sleep(5)
       a = input()
       if a == "q":
              i = i+1


