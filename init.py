import openai

# Set up your OpenAI API credentials
openai.api_key = "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"

def perform_ner(input_speech):
    # Call the OpenAI API for NER
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=f"Perform NER on the following speech: \n\n{input_speech}\n\nThe named entities recognized are:",
      temperature=0.5,
      max_tokens=1024,
      n=1,
      stop=None
    )
    
    # Extract the recognized named entities from the API response
    named_entities = response.choices[0].text.strip()
    
    return named_entities

# Input speech for NER
input_speech = """
Namaskar Excellencies, heads of state, Academics, Business leaders, Policy makers, and my dear friends from all over the world! My greetings to everyone.Welcome to India! First of all, I would like to congratulate the Coalition for Disaster Resilient Infrastructure. The occasion of the 5th edition of the International Conference on Disaster Resilient Infrastructure, ICDRI-2023, is indeed a special one.Friends,The CDRI arose from a global vision. In a closely connected world, the impact of disasters will not just be local. Disasters in one region can have a big impact on a completely different region. Therefore, our response has to be integrated, not isolated.Friends,In just a few years, over 40 countries have become part of the CDRI. This conference is becoming an important platform. Advanced economies and developing economies, large and small countries, The Global North and the Global South, are coming together at this forum. It is also encouraging that it is not just governments that are involved. Global institutions, domain experts and the private sector also play a role.Friends, As we discuss infrastructure, some priorities have to be remembered. The CDRI's theme for this year's conference is related to Delivering Resilient and Inclusive Infrastructure. Infrastructure is not only about returns but also about reach and resilience. Infrastructure must leave none behind and serve the people even during times of crisis. Further, a holistic view of infrastructure is needed. Social and digital infrastructure are as important as transport infrastructure.Friends,During disasters, it is natural that our hearts go out to those who are suffering. Relief and rescue take priority and rightly so. Resilience is about how quickly systems can ensure the return of normal life. Resilience is built in the times between one disaster and another. Studying past disasters and learning lessons from them is the way. This is where the CDRI and this conference play a key role.Friends,Each nation and region faces disasters of different kinds. Societies evolve local knowledge related to infrastructure that can with-stand disasters. While modernizing infrastructure, such knowledge needs to be used intelligently. Modern technology with local insights can be great for resilience. Further, if documented well, local knowledge may become a global best practice!Friends,Some of the initiatives of the CDRI are already showing its inclusive intent. The Infrastructure for Resilient Island States initiative or IRIS benefits many island nations. These islands may be small, but every human living in them matters to us. Just last year, the Infrastructure Resilience Accelerator Fund was announced. This 50 million dollar fund has generated immense interest among developing nations. The commitment of financial resources is key to the success of initiatives.Friends,Recent disasters have reminded us of the scale of challenges we face. Let me give you a few examples. We had heat waves across India and Europe. Many island  nations were harmed by earth-quakes, cyclones and volcanoes. Earth-quakes in Türkiye and Syria caused great loss of lives and property. Your work is becoming more relevant. There are great expectations from the CDRI.Friends,This year, India is also bringing the world together through its G20 presidency. As the president of G20, we have already included the CDRI in many working groups. The solutions you explore here will receive attention at the highest levels of global policy-making. This is an opportunity for CDRI to contribute to infrastructure resilience, especially against climate risks and disasters. I am confident that the deliberations at ICDRI 2023 will provide a pathway to achieve the shared vision of a more resilient world."
"""

# Call the NER function and print the recognized named entities
result = perform_ner(input_speech)
print("Named Entities:")
print(result)

#require fine tuning 
