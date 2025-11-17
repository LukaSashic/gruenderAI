"""
Sample Assessment Items - Howard's 7 Entrepreneurial Personality Dimensions
German-language items calibrated for Gründungszuschuss context
"""

from irt_cat_engine import PersonalityItem

def create_sample_item_bank():
    """Create sample items for each of Howard's 7 dimensions"""
    
    items = [
        # INNOVATIVENESS Items
        PersonalityItem(
            item_id="INNOV_001",
            dimension="innovativeness",
            text_de="Ich entwickle gerne völlig neue Lösungsansätze, auch wenn bewährte Methoden existieren",
            text_en="I enjoy developing completely new approaches, even when proven methods exist",
            discrimination=1.4,
            difficulty_thresholds=[-1.2, -0.3, 0.4, 1.3]
        ),
        
        PersonalityItem(
            item_id="INNOV_002", 
            dimension="innovativeness",
            text_de="Ich experimentiere gerne mit unkonventionellen Geschäftsideen",
            text_en="I enjoy experimenting with unconventional business ideas",
            discrimination=1.6,
            difficulty_thresholds=[-0.8, 0.0, 0.8, 1.6]
        ),
        
        # RISK_TAKING Items
        PersonalityItem(
            item_id="RISK_001",
            dimension="risk_taking", 
            text_de="Ich bin bereit, finanzielle Risiken einzugehen, wenn die Chancen vielversprechend sind",
            text_en="I am willing to take financial risks when opportunities are promising",
            discrimination=1.3,
            difficulty_thresholds=[-1.0, -0.2, 0.6, 1.4]
        ),
        
        PersonalityItem(
            item_id="RISK_002",
            dimension="risk_taking",
            text_de="Ich würde auch bei unsicheren Marktbedingungen ein Unternehmen gründen", 
            text_en="I would start a business even under uncertain market conditions",
            discrimination=1.5,
            difficulty_thresholds=[-0.5, 0.3, 1.0, 1.8]
        ),
        
        # ACHIEVEMENT_ORIENTATION Items
        PersonalityItem(
            item_id="ACHV_001",
            dimension="achievement_orientation",
            text_de="Ich setze mir bewusst hohe Ziele und arbeite intensiv daran, diese zu erreichen",
            text_en="I deliberately set high goals and work intensively to achieve them",
            discrimination=1.2,
            difficulty_thresholds=[-1.5, -0.5, 0.3, 1.2]
        ),
        
        PersonalityItem(
            item_id="ACHV_002",
            dimension="achievement_orientation", 
            text_de="Erfolg zu haben ist mir wichtiger als ein entspanntes Leben zu führen",
            text_en="Being successful is more important to me than leading a relaxed life",
            discrimination=1.4,
            difficulty_thresholds=[-0.8, 0.0, 0.8, 1.5]
        ),
        
        # AUTONOMY_ORIENTATION Items  
        PersonalityItem(
            item_id="AUTO_001",
            dimension="autonomy_orientation",
            text_de="Ich möchte meine eigenen Entscheidungen treffen, ohne Rücksprache mit Vorgesetzten",
            text_en="I want to make my own decisions without consulting superiors",
            discrimination=1.3,
            difficulty_thresholds=[-1.3, -0.4, 0.4, 1.1]
        ),
        
        # PROACTIVENESS Items
        PersonalityItem(
            item_id="PROACT_001", 
            dimension="proactiveness",
            text_de="Ich erkenne Markttrends früh und handle entsprechend, bevor andere reagieren",
            text_en="I recognize market trends early and act accordingly before others react",
            discrimination=1.5,
            difficulty_thresholds=[-0.9, -0.1, 0.7, 1.4]
        ),
        
        # LOCUS_OF_CONTROL Items
        PersonalityItem(
            item_id="LOC_001",
            dimension="locus_of_control", 
            text_de="Mein Erfolg hängt hauptsächlich von meinen eigenen Anstrengungen ab",
            text_en="My success depends mainly on my own efforts",
            discrimination=1.1,
            difficulty_thresholds=[-1.8, -0.8, 0.2, 1.0]
        ),
        
        # SELF_EFFICACY Items
        PersonalityItem(
            item_id="SELF_001",
            dimension="self_efficacy",
            text_de="Ich traue mir zu, auch schwierige Geschäftsprobleme erfolgreich zu lösen",
            text_en="I believe I can successfully solve even difficult business problems",
            discrimination=1.2,
            difficulty_thresholds=[-1.4, -0.6, 0.3, 1.3]
        )
    ]
    
    return items

# Test the item bank
if __name__ == "__main__":
    from irt_cat_engine import IRTCATEngine
    
    print("🧪 Testing Sample Item Bank...")
    items = create_sample_item_bank()
    engine = IRTCATEngine()
    
    print(f"✅ Created {len(items)} assessment items")
    
    # Test each dimension
    dimensions = set(item.dimension for item in items)
    print(f"✅ Covering {len(dimensions)} dimensions: {', '.join(dimensions)}")
    
    # Test with sample user (theta = 0.5, response = 4)
    print(f"\nTesting sample responses:")
    for item in items[:3]:  # Test first 3 items
        prob = engine.grm_probability(0.5, item, 4)
        print(f"✅ {item.dimension}: {prob:.3f} probability for response 4")
    
    print("\n🎉 Sample item bank working!")